import pytest


@pytest.fixture(scope="class")

def setup():
    print("I will be executing first")
    yield
    print("I will execute last")


@pytest.fixture()

def dataload():
    print("Use profile")
    return ['sal','salona','salonanizam.com']

@pytest.fixture(params=[("chrome","sal","bye"),("firefox","salona"),("IE","search")])
def crossbrowser(request):
    return request.param

