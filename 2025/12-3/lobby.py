from collections import deque


def max_joltage(filepath: str, friction: bool = False) -> int:
    total = 0
    with open(filepath) as f:
        for line in f:
            bank = line.strip()
            total += (
                compute_friction_joltage(bank) if friction else compute_joltage(bank)
            )
    return total


def compute_joltage(bank: str) -> int:
    n = len(bank)
    if n <= 2:
        return int(bank)

    joltage = bank[0:2]
    for i in range(1, n):
        if int(bank[i]) > int(joltage[0]) and i != n - 1:
            joltage = bank[i] + bank[i + 1]
        elif int(bank[i]) > int(joltage[1]):
            joltage = joltage[0] + bank[i]
    return int(joltage)


def compute_friction_joltage(bank: str) -> int:
    joltage = []
    deletions = len(bank) - 12
    for n in bank:
        while len(joltage) > 0 and n > joltage[-1] and deletions > 0:
            joltage.pop()
            deletions -= 1
        joltage.append(n)

    while deletions > 0:
        joltage.pop()
        deletions -= 1
    return int("".join(joltage))


if __name__ == "__main__":
    print(f"Part 1:\nTotal output joltage: {max_joltage("lobby.txt")}\n")
    print(f"Part 2:\nTotal output joltage (static friction): {max_joltage("lobby.txt", friction=True)}")
