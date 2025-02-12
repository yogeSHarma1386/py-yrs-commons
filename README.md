# My Package

This is a sample Python package that can be installed locally to a system.

![Codecov](https://codecov.io/gh/yogeSHarma1386/py-yrs-commons/branch/main/graph/badge.svg)
![Coverage Status](https://coveralls.io/repos/github/yogeSHarma1386/py-yrs-commons/badge.svg?branch=main)

## Installation of the package

For local installation, create a wheel and install it:
```bash

# Install build tools
pip install wheel build

# Build the package
python -m build

# Install globally
pip install dist/yrs_commons-0.1.0-py3-none-any.whl
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
