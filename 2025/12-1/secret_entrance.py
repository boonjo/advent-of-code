MAX_POSITION = 99
START_POSITION = 50


def rotate(position: int, direction: str, steps: int) -> int:
    """Returns the new position after rotation"""
    if direction == "L":
        position = (position - steps) % (MAX_POSITION + 1)
    else:
        position = (position + steps) % (MAX_POSITION + 1)

    return position


def get_password(filepath: str, method="default"):
    """Count number of times position is 0 while rotating"""
    position = START_POSITION
    password = 0

    with open(filepath) as f:
        for line in f:
            instr = line.strip()
            direction, steps = instr[0], int(instr[1:])

            if method == "0x434C49434B":
                for _ in range(steps):
                    position = rotate(position, direction, 1)
                    if position == 0:
                        password += 1
            else:
                position = rotate(position, direction, steps)
                if position == 0:
                    password += 1

    return password


if __name__ == "__main__":
    print(f"Part 1:\nSecret Entrance Password: {get_password("secret-entrance.txt")}\n")
    print(f"Part 2:\nSecret Entrance Password using method 0x434C49434B: {get_password("secret-entrance.txt", method="0x434C49434B")}")
