def get_invalids(filepath: str, exact_twice: bool = False) -> int:
    total_invalid = 0

    with open(filepath) as f:
        product_ids = f.readline().strip()

        for id_range in product_ids.split(","):
            lower, upper = id_range.split("-")
            total_invalid += sum_invalid_range(int(lower), int(upper), exact_twice)

    return total_invalid


def sum_invalid_range(lower: int, upper: int, exact_twice: bool = False) -> int:
    invalids = 0
    for id in range(lower, upper + 1):
        if check_repeats(str(id), exact_twice):
            invalids += id

    return invalids


def check_repeats(num: str, exact_twice: bool = False) -> bool:
    length = len(num)
    if length == 1:
        return False

    if exact_twice:
        if length % 2:
            return False
        half = length // 2
        return num[half:] == num[:half]
    else:
        # if num consists of smaller sub-integers,
        # then the sub-integers will appear again inside its own doubled form
        repeat = (num + num).find(num, 1)
        return repeat < length


if __name__ == "__main__":
    print(f"Part 1:\nAdding up all twice repeated invalid IDs produces {get_invalids("gift_shop.txt", exact_twice=True)}\n")
    print(f"Part 2:\nAdding up all repeated invalid IDs produces {get_invalids("gift_shop.txt")}")
