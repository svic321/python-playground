import pytest

from python_playground.leetcode.leet_925_long_pressed_name import Solution


@pytest.mark.parametrize(
    "name, typed, expected",
    [
        ("alex", "aaleex", True),
        ("saeed", "ssaaedd", False),
        ("alex", "alex", True),
        ("laiden", "laiden", True),
        ("a", "aaaa", True),
        ("abc", "aabbcc", True),
        ("alex", "aaleexa", False),
        ("alex", "alexxr", False),
        ("alex", "alx", False),
        ("alex", "ale", False),
        ("abc", "xabc", False),
        ("abc", "", False),
        ("a", "b", False),
    ],
)
def test_is_long_pressed_name(name, typed, expected):
    assert Solution().isLongPressedName(name, typed) is expected


@pytest.mark.benchmark(group="isLongPressedName")
def test_benchmark_is_long_pressed_name(benchmark):
    name = "abcdefghij" * 50
    typed = "".join(c * 3 for c in name)
    assert benchmark(Solution().isLongPressedName, name, typed) is True
