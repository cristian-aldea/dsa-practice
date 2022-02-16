

def get_bit(num: int, i: int):
    return 0 if (num & (1 << i)) == 0 else 1


def set_bit(num: int, i: int):
    return num | (1 << i)


def unset_bit(num: int, i: int):
    return num & ~(1 << i)

def update_bit(num: int, i: int, v: bool):
    return set_bit(num, i) if v else unset_bit(num,i)


if __name__ == "__main__":
    num = 37

    print(f"For {num} -> {bin(num)}")
    print(f"first bit: {get_bit(num, 0)}")
    print(f"second bit: {get_bit(num, 1)}")
    print(f"third bit: {get_bit(num, 2)}")
    print(f"fourth bit: {get_bit(num, 3)}")
    print(f"fifth bit: {get_bit(num, 4)}")

    print("Setting fifth bit")
    num = set_bit(num, 4)
    print(f"Now: {num} -> {bin(num)}")

    print("Unsetting fifth bit")
    num = unset_bit(num, 4)
    print(f"Now: {num} -> {bin(num)}")
