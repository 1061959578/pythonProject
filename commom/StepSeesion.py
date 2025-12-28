# conding: utf-8
# @Time : 2025/12/22下午4:33
# @Author : shiqing.duan

from Globals import Globals
from commom.StepPortal import StepPortal

class Stepseesion(StepPortal):
    def step_login(self,set_param = None):
        headers = {
            'Content-Type': 'application/json',
            'cookie': None,
            "bank-admin-token": None
        }
        data = self.parse_param_data(set_param)

        url = 'https://grc-admin-sit1.test-stable.npt.maribank.io/api/session/credential/v1/login'
        response = self.call_api(url,method='Post',json= data,headers=headers)
        print('输出reponse',response.json())
        # response = requests.post(url, json=data, headers=headers)
        assert response.json()['msg'] == 'success'


        # 通过全局变量Globals ，设置Admin Portal登录token，供其他接口使用
        # bank_admin_token = response.json()['data']
        # cookie = 'bank-admin-token=' + bank_admin_token
        Globals.admin_portal['bank-admin-token'] = response.json()['data']
        Globals.admin_portal['cookie'] = 'bank-admin-token=' + response.json()['data']

        return response