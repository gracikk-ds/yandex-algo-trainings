def station_counter(
        total_station_number=None,
        home_station=None,
        work_station=None,
) -> int:
    """
    Count station between points in a circle
    :param total_station_number: Number of station in a circle
    :param home_station: start station
    :param work_station: end station
    :return: number of stations to overcome
    """
    if total_station_number is None:
        total_station_number, home_station, work_station = map(int, input().split(" "))
    assert total_station_number <= 100
    middle_point = total_station_number / 2
    forward_path = abs(work_station - home_station)
    if forward_path >= middle_point:
        backward_path = total_station_number - forward_path
        return backward_path - 1
    else:
        return forward_path - 1


if __name__ == "__main__":
    result = station_counter()
    print(result)
