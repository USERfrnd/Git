import pytest


#

@pytest.mark.usefixtures("setup")

class TestExample:

    def test_examplee(self):
        print("Execute")

    def test_example1(self):
        print("Method")

    def test_example2(self):
        print("Home")