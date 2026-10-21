import pytest

from python_playground.leetcode.leet_20_valid_parentheses import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("{[]}", True),
        ("", True),
        ("((()))", True),
        ("([{}])", True),
        ("(]", False),
        ("([)]", False),
        ("(", False),
        ("]", False),
        ("(()", False),
        ("{[}", False),
        ("((()))]", False),
        ("abc", False),
    ],
)
def test_is_valid(s, expected):
    assert Solution().isValid(s) is expected


@pytest.mark.benchmark(group="isValid")
def test_benchmark_is_valid(benchmark):
    s = "(" * 500 + "[" * 500 + "{" * 500 + "}" * 500 + "]" * 500 + ")" * 500
    assert benchmark(Solution().isValid, s) is True
