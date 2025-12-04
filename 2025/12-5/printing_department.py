NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def roll_grid(filepath: str, keep_removing: bool = False) -> int:
    grid = []
    with open(filepath) as f:
        for line in f:
            grid.append(list(line.rstrip("\n")))

    roll, grid = roll_access(grid)
    if keep_removing:
        total = 0
        while roll != 0:
            total += roll
            roll, grid = roll_access(grid)

        return total

    else:
        return roll


def roll_access(grid: list[list[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    access = 0

    remove = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            adj = 0
            for dr, dc in NEIGHBOURS:
                mv_r, mv_c = r + dr, c + dc

                if 0 <= mv_r < rows and 0 <= mv_c < cols and grid[mv_r][mv_c] == "@":
                    adj += 1

            if adj < 4:
                access += 1
                remove.append((r, c))

    for r, c in remove:
        grid[r][c] = "x"

    return access, grid


if __name__ == "__main__":
    print(f"Part 1:\nAccessible Paper Rolls: {roll_grid("printing_department.txt")}\n")
    print(f"Part 2:\nAccessible Paper Rolls: {roll_grid("printing_department.txt", keep_removing=True)}\n")
