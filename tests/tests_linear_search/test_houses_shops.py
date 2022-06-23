from algorithms.linear_search import houses_shops


def test_houses_shops():
    """
    Test for houses_shops programme
    :return: None
    """
    test_case_1 = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 2], 9]
    test_case_2 = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 1], 9]
    test_case_3 = [[1, 0, 0, 0, 0, 2, 0, 0, 0, 1], 5]
    test_case_4 = [[2, 0, 1, 1, 0, 1, 0, 2, 1, 2], 3]
    test_case_5 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 9]
    test_case_6 = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 1], 1]

    test_container = [
        test_case_1, test_case_2, test_case_3,
        test_case_4, test_case_5, test_case_6]

    for test_case in test_container:
        variables, result_target = test_case
        result_program = houses_shops.houses_shops(variables)
        assert result_target == result_program
