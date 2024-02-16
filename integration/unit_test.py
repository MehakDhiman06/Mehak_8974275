from testcase import expected_pass_value, actual_pass_value, expected_fail_value, actual_fail_value


def test_pass():
    if expected_pass_value == actual_pass_value:
        assert True
    else:
        assert False, "Test failed: Expected value does not match actual value"


def test_fail():
    if expected_fail_value == actual_fail_value:
        assert True
    else:
        assert False, "Test failed: Expected value does not match actual value"