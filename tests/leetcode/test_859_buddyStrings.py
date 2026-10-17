import pytest

from python_playground.leetcode.leet_859_buddyStrings import Solution


@pytest.mark.parametrize(
    "s, goal, expected",
    [
        ("ab", "ba", True),
        ("ab", "ab", False),
        ("aa", "aa", True),
        ("aaaaaaabc", "aaaaaaacb", True),
        ("abcd", "abdc", True),
        ("abcaa", "abcbb", False),
        ("abc", "abcd", False),
        ("", "", False),
        ("a", "a", False),
        ("abab", "abab", True),
        ("abc", "bca", False),
        ("abcd", "badc", False),
    ],
)
def test_buddy_strings(s, goal, expected):
    assert Solution().buddyStrings(s, goal) is expected


@pytest.mark.benchmark(group="buddyStrings")
def test_benchmark_buddy_strings(benchmark):
    s = "a" * 1000 + "bc"
    goal = "a" * 1000 + "cb"
    assert benchmark(Solution().buddyStrings, s, goal) is True
