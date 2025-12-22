# conding: utf-8
# @Time : 2025/12/22下午4:33
# @Author : shiqing.duan
import requests
from Globals import Globals
from step.commom.StepPortal import StepPortal

class Stepseesion(StepPortal):
    def step_login(self):
        headers = {
            'Content-Type': 'application/json',
            'cookie': None,
            "bank-admin-token": None
        }
        data = {
            "password": "5AEA19BDBF0350E6028DFFF43FAD46C7",
            "userId": "reviewer1"
        }
        url = 'https://grc-admin-sit1.test-stable.npt.maribank.io/api/session/credential/v1/login'
        response = self.call_api(url,json= data,headers=headers)
        # response = requests.post(url, json=data, headers=headers)


        # 通过全局变量Globals ，设置Admin Portal登录token，供其他接口使用
        # bank_admin_token = response.json()['data']
        # cookie = 'bank-admin-token=' + bank_admin_token
        Globals.admin_portal['bank-admin-token'] = response.json()['data']
        Globals.admin_portal['cookie'] = 'bank-admin-token=' + response.json()['data']

        return response