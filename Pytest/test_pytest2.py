import pytest


def test_login():
    print('Login Successful First')

@pytest.mark.regression
def test_logout():
    print('Logout Successful First')

@pytest.mark.sanity
def test_verify():
    assert 2+2==4
