# My Package

This is a sample Python package that can be installed globally.

## Installation

```bash
pip install yrs_commons
```

## Usage

```python
from yrs_commons import MyClass, my_function, utility_function

# Create instance of MyClass
obj = MyClass()
print(obj.greet())

# Use the function
print(my_function())
```

### Updating / Creating dist wheel again

Install in development mode (for testing):
```bash
cd ~/Softwares/Scripts/yrs_commons
pip install -e .
```

For global installation, create a wheel and install it:
```bash
# Install build tools
pip install wheel build

# Build the package
python -m build

# Install globally
pip install dist/yrs_commons-0.1.0-py3-none-any.whl
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

