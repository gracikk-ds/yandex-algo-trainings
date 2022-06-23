def count_max(seq=None) -> int:
    """
    Count max elements in seq
    :param seq: list of elements
    :return: number of elements equal to maximum
    """
    if seq is None:
        seq = list(map(int, input().split(" ")))

    index_of_zero = seq.index(0)
    seq = seq[:index_of_zero]

    max_value = 0
    for element in seq:
        if element > max_value:
            max_value = element

    max_values_count = 0
    for element in seq:
        if element == max_value:
            max_values_count += 1

    return max_values_count


if __name__ == "__main__":
    result = count_max()
    print(result)
