def stones(
        bench_length=None,
        stones_positions=None
):
    """
    List the blocs that we have to leave
    :param bench_length: length of bench
    :param stones_positions: position of those stones relatively
    to the left edge of the bench
    :return: positions of blocs
    """
    if bench_length is None:
        bench_length, amount_stones = list(map(int, input().split()))
        stones_positions = list(map(int, input().split()))

    if bench_length % 2 and ((bench_length // 2) in stones_positions):
        print(bench_length // 2)
        return bench_length // 2
    else:
        stones_positions.append(bench_length / 2)
        stones_positions.sort()
        index = stones_positions.index(bench_length / 2)
        left_bloc = int(stones_positions[index-1])
        right_bloc = int(stones_positions[index+1])
        print(left_bloc, right_bloc)
        return [left_bloc, right_bloc]


if __name__ == "__main__":
    result = stones()
