from algorithms.complexity_testing import dates


def test_dates_checker():
    """
    Test for dates_checker programme
    :return: None
    """
    test_case_1 = [[31, 12, 2012], 1]
    test_case_2 = [[12, 31, 2012], 1]
    test_case_3 = [[1, 1, 2012], 1]
    test_case_4 = [[12, 12, 2012], 1]
    test_case_5 = [[1, 2, 2003], 0]
    test_case_6 = [[2, 29, 2008], 1]

    test_container = [
        test_case_1,
        test_case_2,
        test_case_3,
        test_case_4,
        test_case_5,
        test_case_6,
    ]

    for test_case in test_container:
        variables, result_target = test_case
        result_program = dates.dates_checker(*variables)
        assert result_target == result_program
