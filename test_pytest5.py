import pytest

@pytest.mark.fixture()
def pre_post():
    print("precondition")
    yield
    print("postcondition")

def test_m1(pre_post):
    print("teststeps")
def test_m2(pre_post):
    print("teststeps")
def test_m3(pre_post):
    print("teststeps")
def test_m4(pre_post):
    print("teststeps")