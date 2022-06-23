def houses_shops(seq=None) -> int:
    """
    Find max distance between house and shop
    :param seq: list of building's types
    :return: max distance
    """
    if seq is None:
        seq = list(map(int, input().split(" ")))

    list_of_shops = [
        shop_index for shop_index in range(len(seq)) if seq[shop_index] == 2
    ]

    max_distance = 0
    for i, element in enumerate(seq):
        if element == 1:
            distance = min([abs(shop_index - i) for shop_index in list_of_shops])
            if distance > max_distance:
                max_distance = distance

    return max_distance


if __name__ == "__main__":
    result = houses_shops()
    print(result)
