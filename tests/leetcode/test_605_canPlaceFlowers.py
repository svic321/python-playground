import pytest

from python_playground.leetcode.leet_605_canPlaceFlowers import Solution

METHODS = ["canPlaceFlowers", "canPlaceFlowers_1", "canPlaceFlowers_2"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "flowerbed, n, expected",
    [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([0], 1, True),
        ([1], 1, False),
        ([1], 0, True),
        ([0, 0], 1, True),
        ([0, 0], 2, False),
        ([0, 0, 0], 2, True),
        ([0, 0, 0], 3, False),
        ([1, 0, 1, 0, 1], 1, False),
        ([1, 0, 1, 0, 1, 0, 1], 0, True),
        ([0, 0, 1, 0, 0], 2, True),
        ([0, 0, 1, 0, 0], 3, False),
        ([0, 1, 0], 1, False),
        ([0, 0, 0, 0, 0, 0, 0], 4, True),
        ([0, 0, 0, 0, 0, 0, 0], 5, False),
    ],
)
def test_can_place_flowers(method, flowerbed, n, expected):
    # The first method mutates its input, so pass a copy
    assert getattr(Solution(), method)(list(flowerbed), n) is expected


@pytest.mark.benchmark(group="canPlaceFlowers")
@pytest.mark.parametrize("method", METHODS)
def test_benchmark_can_place_flowers(benchmark, method):
    flowerbed = [0, 0, 1, 0] * 250
    func = getattr(Solution(), method)
    # Fresh copy per call because canPlaceFlowers mutates the list
    result = benchmark.pedantic(
        lambda fb: func(fb, 250),
        setup=lambda: ((list(flowerbed),), {}),
        rounds=1000,
    )
    assert result is True
