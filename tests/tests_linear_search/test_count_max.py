from algorithms.linear_search import count_max


def test_count_max():
    """
    Test for count_max programme
    :return: None
    """
    test_case_1 = [[0], 0]
    test_case_2 = [[1, 2, 3, 3, 0], 2]
    test_case_3 = [[1, 1, 1, 1, 0], 4]
    test_case_4 = [[1, 3, 3, 1, 0], 2]

    test_container = [test_case_1, test_case_2, test_case_3, test_case_4]

    for test_case in test_container:
        variables, result_target = test_case
        result_program = count_max.count_max(variables)
        assert result_target == result_program
