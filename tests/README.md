# Tests

Tests use [pytest](https://docs.pytest.org) and [pytest-benchmark](https://pytest-benchmark.readthedocs.io). The folder mirrors the package layout, e.g. [leetcode/test_13_romToInt.py](leetcode/test_13_romToInt.py) tests `src/python_playground/leetcode/leet_13_romToInt.py`.

Each test file contains two kinds of tests:

- **Correctness tests**: parametrized checks of expected results.
- **Benchmark tests**: named `test_benchmark_*`, they measure execution time of each method.

## Commands

Run from the project root.

| Goal | Command |
|---|---|
| Everything (tests + benchmarks) | `uv run pytest` |
| Only tests, no benchmark | `uv run pytest --benchmark-skip` |
| Only benchmarks | `uv run pytest --benchmark-only` |

Alternative for skipping benchmarks by name:

```bash
uv run pytest -k "not benchmark"
```

### Single file

```bash
uv run pytest tests/leetcode/test_13_romToInt.py --benchmark-skip
uv run pytest tests/leetcode/test_13_romToInt.py --benchmark-only
```

### Grouping the benchmark report

```bash
uv run pytest tests/leetcode/test_13_romToInt.py --benchmark-only --benchmark-group-by=param
```

- `--benchmark-only` runs only the benchmark tests.
- `--benchmark-group-by=param` groups the results in the report by the test's **parametrize value** and overrides the `group` set in `@pytest.mark.benchmark(group=...)`.

In `test_benchmark_roman_to_int` the only parameter is `method` (`romanToInt` or `romanToInt_best`), so this produces **one table per method** with a single row each. Rows in different tables are not ranked against each other, so there is no relative comparison (no `1.0`/`1.05` ratios).

To compare the methods side by side, omit the flag. The default is `--benchmark-group-by=group`, which uses the `group="romanToInt"` marker on the test, so both methods land in one table:

```bash
uv run pytest tests/leetcode/test_13_romToInt.py --benchmark-only
```

Use `--benchmark-group-by=param` when a benchmark has several parameters, such as different inputs, and you want to compare the methods per input. In that case, make sure the parameter you want to group on is the one that varies across the compared tests. Other options are `func`, `fullname`, `name` and `param:NAME` (group by one specific parameter, e.g. `param:method`).

## Reading the benchmark report

The report ranks the methods in each benchmark group. Compare the **Median** column; **Min** and **Max** are sensitive to outliers. Values in parentheses are relative to the best result (`1.0` is the fastest).
