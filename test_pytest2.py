import pytest

@pytest.fixture()
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



    #@pytest.mark.parametrize("a,b,c",[(2,3,5),(12,13,25),(120,130,250)])
#def test_m1(a,b,c):
    #assert a+b==c


#def test_m1():
    a= 5
    b= 4
    assert a + b ==9

#def test_m2():
    a=12
    b=13
    assert a+b==25

#def test_m3():
    a=130
    b=120
    assert a+b==250
