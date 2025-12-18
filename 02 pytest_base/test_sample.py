import os

import pytest


# content of tests/test_something_else.py
def test_username(parametrized_username):
    assert parametrized_username in ['one', 'two', 'three']


def test_username(non_parametrized_username):
    assert non_parametrized_username == 'username'



market = "ID"

@pytest.mark.skipif(market=="ID",reason= "该市场无该功能")
def test_add_user():
    assert 3 == 1



@pytest.mark.skip(reason="测试用例尚未完成")
def test_function():
    assert 1 + 1 == 3

@pytest.mark.skip
def test_another():
    pass

@pytest.mark.xfail(raises = ZeroDivisionError)
def test_dmoe_xfail():
    assert 6/0 == 3


@pytest.mark.xfail(run=False, reason="暂时不运行")
def test_skip_execution():
    print("这行不会执行")
    assert False

@pytest.mark.xfail("hasattr(os, 'sep')")
def test_hello3():
    assert 0
