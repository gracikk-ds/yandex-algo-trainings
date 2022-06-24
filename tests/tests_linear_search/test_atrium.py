from algorithms.linear_search import atrium


def test_atrium():
    """
    Test for atrium programme
    :return: None
    """
    test_case_1 = [[5, [0, 2]], 2]
    test_case_2 = [[13, [1, 4, 8, 11]], [4, 8]]
    test_case_3 = [[14, [1, 6, 8, 11, 12, 13]], [6, 8]]

    test_container = [test_case_1, test_case_2, test_case_3]

    for test_case in test_container:
        variables, result_target = test_case
        result_program = atrium.stones(variables[0], variables[1])
        assert result_target == result_program
