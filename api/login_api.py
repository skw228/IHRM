import requests
from requests import Response


# 创建封装的接口类
class LoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

    def login(self, jsondata, headers):
        """
        :rtype:Response
        :param jsondata:
        :param headers:
        :return:
        """
        # 发送登录请求，并返回
        return requests.post(url=self.login_url, json=jsondata, headers=headers)
