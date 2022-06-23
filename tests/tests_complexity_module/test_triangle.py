from algorithms.complexity_testing import triangle


def test_triangle_task():
    """
    Test for triangle_task programme
    :return: None
    """
    test_case_1 = [[5, [-5, 5]], 3]
    test_case_2 = [[5, [1, 1]], 0]
    test_case_3 = [[3, [-1, -1]], 1]
    test_case_4 = [[4, [4, 4]], 2]
    test_case_5 = [[4, [2, 2]], 0]
    test_case_6 = [[5, [10, 0]], 2]

    test_container = [
        test_case_1, test_case_2, test_case_3,
        test_case_4, test_case_5, test_case_6
    ]

    for test_case in test_container:
        variables, result_target = test_case
        result_program = triangle.triangle_task(*variables)
        assert result_target == result_program
