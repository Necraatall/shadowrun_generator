import pytest

#spustenim testu python -m pytest -v test_secteni.py

def secti(a, b):

    neco = a+b
    return  neco, a, b

def test_secti():

    if (secti(3,4)[1] == secti(3,4)[2]):
        raise AssertionError('Test selhal! 1')

    if not (secti(1,2)[0] == 3):
        raise AssertionError('Test selhal! 2')

def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()        