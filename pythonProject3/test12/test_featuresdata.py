import pytest

from test12.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):

    def test_example(self,dataload):
        log = self.test_loggingDemo
        log.debug(dataload[1])
        print(dataload[0])
