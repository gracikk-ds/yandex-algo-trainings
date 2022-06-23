def dates_checker(
    x=None,
    y=None,
    z=None,
) -> int:
    """
    Check dates format
    :param x: day or month
    :param y: day or month
    :param z: year
    :return: 1 if we could identify date format type and 0 if not
    """
    if x is None:
        x, y, z = map(int, input().split(" "))

    if (x > 12) or (y > 12) or (y == x):
        return 1
    else:
        return 0


if __name__ == "__main__":
    result = dates_checker()
    print(result)
