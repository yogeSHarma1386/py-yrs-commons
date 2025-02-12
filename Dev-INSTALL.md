## Code setup

```bash

virtualenv .venv
pipenv install -r requirements.txt
```

## Run Tests

Run all tests:

```bash
pytest
```

Run specific test types:

```bash
# Run unit tests only
pytest -v -m unit

# Run integration tests
pytest -v -m integration

# Run performance tests
pytest -v -m performance
```

Run tests in parallel:

```bash
pytest -n auto  # Uses pytest-xdist
```

Run with coverage:

```bash
pytest --cov=yrs_commons --cov-report=html
```

Run tests across multiple Python versions:

```bash
tox
```

Run specific test files or classes:

```bash
# Run specific file
pytest tests/unit/test_module1.py

# Run specific class
pytest tests/unit/test_module1.py::TestModule1

# Run specific test
pytest tests/unit/test_module1.py::TestModule1::test_function1
```

#### UT help

Configuration:

```
pytest.ini for pytest configuration
tox.ini for multi-environment testing
conftest.py for shared fixtures
```

Test Markers:

```python
import pytest


@pytest.mark.unit
@pytest.mark.integration
@pytest.mark.performance
@pytest.mark.slow
def sample_test():
    pass
```

## Lint checker

```bash
source .venv/bin/activate && $(which python3) -m flake8 yrs_commons
```
