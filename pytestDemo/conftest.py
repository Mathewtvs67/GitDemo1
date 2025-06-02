import pytest


@pytest.fixture(scope='class')
def setup():
    print('will be called first')
    yield
    print('will be called last')

@pytest.fixture()
def loaddata():
    print('loading data')
    return['sunil','mathew','mathew.us@hotmail.com']