import pytest

def test_login():
    print('Login Successful')

def test_logout():
    print('Logout Successful')

@pytest.mark.sanity
def test_verify():
    assert 2+2==4
