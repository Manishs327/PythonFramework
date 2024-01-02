import pytest

##Parametrize a fixture
# @pytest.fixture(params=["a","b"])
# def demo_fixture(request):
#     print(request.param)

##Parametrize using mark.parametrize
@pytest.mark.parametrize("a, b, final",[(1,2,3),(5,5,11),(1,1,2)])
def testLogin(a, b, final):
    print('Login Successful')
    assert a+b==final
