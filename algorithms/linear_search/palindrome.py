import math


def palindrome(string=None) -> int:
    """
    Create palindrome from string
    :param string: string to fix
    :return: max distance
    """
    if string is None:
        string = input()

    string_lenth = len(string)

    left_side = string[: math.floor(string_lenth / 2)]
    right_side = string[math.ceil(string_lenth / 2) :]

    payment = 0
    for i, j in zip(left_side, right_side[::-1]):
        if i != j:
            payment += 1

    return payment


if __name__ == "__main__":
    result = palindrome()
    print(result)
