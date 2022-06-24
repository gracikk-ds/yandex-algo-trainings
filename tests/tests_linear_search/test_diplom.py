from algorithms.linear_search import diplom


def test_diplom():
    """
    Test for diplom programme
    :return: None
    """
    test_case_1 = [[2, [2, 1]], 1]
    test_case_2 = [[5, [10, 1, 34, 4, 8]], 23]
    test_case_3 = [[1, [10]], 0]

    test_container = [test_case_1, test_case_2, test_case_3]

    for test_case in test_container:
        variables, result_target = test_case
        result_program = diplom.diploma_time(variables[0], variables[1])
        assert result_target == result_program
