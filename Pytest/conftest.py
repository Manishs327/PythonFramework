import pytest

#fixture where scope is session
@pytest.fixture(scope="session",autouse=True)
def setUp():
    print('Connect DB')

#fixture where scope is method
@pytest.fixture(autouse=True)
def setUp1(browser):
    if(browser=="chrome"):
        print('Launch Chrome Browser')
    elif(browser=='firefox'):
        print('Launch Firefox Browser')
    else:
        print('Provide valid Browser')

    yield
    print('Close browser')

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



