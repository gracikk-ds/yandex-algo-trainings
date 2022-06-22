from algorithms.complexity_testing import circle_line


def test_station_counter():
    """
    Test for station_counter programme
    :return: None
    """
    test_case_1 = [[100, 5, 6], 0]
    test_case_2 = [[10, 1, 9], 1]
    test_case_3 = [[10, 9, 1], 1]

    test_container = [test_case_1, test_case_2, test_case_3]

    for test_case in test_container:
        variables, result_target = test_case
        result_program = circle_line.station_counter(*variables)
        assert result_target == result_program
