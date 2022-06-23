from algorithms.complexity_testing import school_building


def test_school_geo_plan():
    """
    Test for school_geo_plan programme
    :return: None
    """
    test_case_1 = [[4, [1, 2, 3, 4]], 2]
    test_case_2 = [[3, [-1, 0, 1]], 0]
    test_case_3 = [[4, [-6, -4, -2, 0]], -4]
    test_case_4 = [[3, [-10, -4, 5]], -4]
    test_case_5 = [[0, []], 0]
    test_case_6 = [[1, [10]], 10]

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
        result_program = school_building.school_geo_plan(*variables)
        assert result_target == result_program
