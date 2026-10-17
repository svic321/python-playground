import pytest

from python_playground.leetcode.leet_13_romToInt import Solution


@pytest.mark.parametrize("method", ["romanToInt", "romanToInt_best"])
@pytest.mark.parametrize(
    "roman, expected",
    [
        ("I", 1),
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("MCMXCIV", 1994),
        ("MMMCMXCIX", 3999),
    ],
)
def test_roman_to_int(method, roman, expected):
    assert getattr(Solution(), method)(roman) == expected