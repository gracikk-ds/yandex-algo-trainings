from algorithms.complexity_testing import interactor


def test_interactor():
    """
    Test for interactor programme
    :return: None
    """
    test_case_1 = [[0, 0, 0], 0]
    test_case_2 = [[-1, 0, 1], 3]
    test_case_3 = [[42, 1, 6], 6]
    test_case_4 = [[44, 7, 4], 1]
    test_case_5 = [[1, 4, 0], 3]
    test_case_6 = [[-3, 2, 4], 2]
    test_case_7 = [[3000, 3000, 3000], "Input Error"]

    test_container = [
        test_case_1,
        test_case_2,
        test_case_3,
        test_case_4,
        test_case_5,
        test_case_6,
        test_case_7,
    ]

    for test_case in test_container:
        variables, result_target = test_case
        result_program = interactor.interactor_verdict(*variables)
        assert result_target == result_program
