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
