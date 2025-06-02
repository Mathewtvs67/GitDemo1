import pytest


#@pytest.mark.skip
@pytest.mark.xfail
def test_Demo1Second():
    msg='Hi'
    assert msg == 'Hi100'

@pytest.mark.smoke
def test_Demo20Second():
    a=5
    b=10
    assert a+5==b
    print('Hi')