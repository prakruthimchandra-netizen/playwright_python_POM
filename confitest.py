import pytest

@pytest.fixture(autouse=True, scope="module")
def pre_post():
    print("precondition")
    yield
    print("postcondition")
