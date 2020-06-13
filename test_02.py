import requests


def test_case_01(one_session):
    """
    登录
    :return:
    """
    url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/login"
    params = {
        "mobilephone": "13877772200",
        "pwd": "123456"
    }
    res = one_session.request(url=url, params=params, method="post")
    assert res.json()["msg"] == "登录成功"


def test_case_02(one_session):
    """
    获取用例列表
    :return:
    """
    url = "http://test.lemonban.com:8080/futureloan/mvc/api/member/list"
    res2 = one_session.request(url=url, method="post")
    assert res2.json()["msg"] == "获取用户列表成功"


if __name__ == '__main__':
    session = requests.Session()
    test_case_01(session)
    test_case_02(session)



