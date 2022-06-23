from algorithms.linear_search import palindrome


def test_palindrome():
    """
    Test for palindrome programme
    :return: None
    """
    test_case_1 = ["a", 0]
    test_case_2 = ["ab", 1]
    test_case_3 = ["abc", 1]
    test_case_4 = ["cognitive", 4]
    test_case_5 = ["abcfcba", 0]
    test_case_6 = ["abccba", 0]

    test_container = [
        test_case_1, test_case_2, test_case_3,
        test_case_4, test_case_5, test_case_6]

    for test_case in test_container:
        variables, result_target = test_case
        result_program = palindrome.palindrome(variables)
        assert result_target == result_program
