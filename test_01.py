import requests
import pytest


def test_case_01():
    """
    登录
    :return:
    """
    url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/register"
    params = {
        "mobilephone": "13877772200",
        "pwd": "123456"
    }
    response = requests.post(url=url, params=params)
    assert response.json()["msg"] == "注册成功"


def test_case_02():
    """
    登录
    :return:
    """
    url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/login"
    params = {
        "mobilephone": "13877772200",
        "pwd": "123456"
    }
    res = requests.post(url=url, params=params)
    assert res.json()["msg"] == "登录成功"


def test_case_03():
    """
    获取用例列表
    :return:
    """
    url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/list"
    res2 = requests.post(url=url)
    assert res2.json()["msg"] == "获取用户列表成功"