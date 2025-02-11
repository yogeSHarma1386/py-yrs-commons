import pathlib
import pytest

@pytest.fixture(scope="session")
def global_resource():
    # Setup global resource
    resource = "test_resource"
    yield resource
    # Cleanup code here

@pytest.fixture(scope="function")
def temp_resource():
    # Setup temporary resource
    resource = {"data": "temp"}
    yield resource
    # Cleanup code here


def pytest_ignore_collect(collection_path: pathlib.Path, config):
    # Convert the path to a string for easier matching
    path_str = str(collection_path)
    # Return True if the file should be ignored
    if "sample" in path_str:
        return True
