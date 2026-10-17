# python-playground

A personal sandbox for learning Python. It is used to solve [LeetCode](https://leetcode.com) problems, document the approaches taken, collect tips & tricks, and cover the solutions with tests.

## Project structure

```
python-playground/
├── src/python_playground/      # Importable package
│   ├── __init__.py             # Package entry point (`main`)
│   ├── explore.py              # Scratch script for quick experiments (VS Code `# %%` cells)
│   └── leetcode/               # LeetCode solutions
│       └── leet_13_romToInt.py # 13. Roman to Integer (two implementations)
├── tests/                      # pytest test suite, mirrors the package layout
│   └── leetcode/
│       └── test_13_romToInt.py # Parametrized tests for both Roman-to-Integer methods
├── notebooks/
│   ├── problems.ipynb          # Problem statements, notes and progress per problem
│   └── tips.ipynb              # Interesting Python snippets and approaches
├── pyproject.toml              # Project metadata, dependencies and tooling
├── .python-version             # Pinned Python version (3.14)
└── uv.lock                     # Locked dependencies (managed by uv)
```

### Details

- [src/python_playground/leetcode/](src/python_playground/leetcode): one module per problem, named `leet_<number>_<name>.py`. Each exposes a `Solution` class like LeetCode does.
  - [leet_13_romToInt.py](src/python_playground/leetcode/leet_13_romToInt.py) provides `romanToInt` (single pass with `zip`) and `romanToInt_best` (right-to-left scan).
- [tests/leetcode/](tests/leetcode): pytest tests for each solution, e.g. [test_13_romToInt.py](tests/leetcode/test_13_romToInt.py), which runs the same cases against both methods.
- [notebooks/problems.ipynb](notebooks/problems.ipynb): write-ups of each problem and my progress.
- [notebooks/tips.ipynb](notebooks/tips.ipynb): reusable tips, such as pairing list items with `zip`.
- [src/python_playground/explore.py](src/python_playground/explore.py): free-form scratch space.

## Requirements

- Python >= 3.14
- [uv](https://docs.astral.sh/uv/) for environment and dependency management
- Dev tools: `pytest`, `ruff`, `ipykernel`

## Getting started

```bash
uv sync                 # create the virtualenv and install dev dependencies
uv run pytest           # run the tests
uv run ruff check .     # lint
uv run python-playground
```

## Adding a new problem

1. Create `src/python_playground/leetcode/leet_<number>_<name>.py` with a `Solution` class.
2. Add `tests/leetcode/test_<number>_<name>.py` with parametrized cases.
3. Document the problem in [notebooks/problems.ipynb](notebooks/problems.ipynb).
