import pytest

from pytestDemo.BaseClass import BaseClass
from pytestDemo.conftest import loaddata


@pytest.mark.usefixtures('setup')
class TestExample(BaseClass):

    def test_myone(self):
        print('in the method one')
    def test_mytwo(self):
        print('in the method two')

    def test_mythree(self):
        print('in the method three')

    def test_myfour(self,loaddata):
        print('in the method four')
        log = self.getLogger()
        log.info(loaddata[0])
        log.info(loaddata[2])
        print(loaddata[0])
        print(loaddata[2])


