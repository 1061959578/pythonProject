# conding: utf-8
# @Time : 2025/12/19下午4:29
# @Author : shiqing.duan
import pytest
import requests
from step.GRC.Param_Management.step_param_management import StepParamManagement
from commom.StepSeesion import Stepseesion

class TestParamManagement(Stepseesion,StepParamManagement):

    def test_login(self):
        headers = {
            'Content-Type': 'application/json',
            "bank-admin-token": None,
            'cookie':None

        }
        data = {
            "password":"5AEA19BDBF0350E6028DFFF43FAD46C7",
            "userId":"reviewer1"
        }
        url = 'https://grc-admin-sit1.test-stable.npt.maribank.io/api/session/credential/v1/login'
        response = requests.post(url, json=data,headers=headers)
        bank_admin_token = response.json()['data']
        cookies = 'bank-admin-token=' + bank_admin_token

        print(bank_admin_token)


    @pytest.fixture
    def get_hearder(self):
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
        response = requests.post(url, json=data, headers=headers)
        bank_admin_token = response.json()['data']
        cookie = 'bank-admin-token=' + bank_admin_token
        headers = {
            'Content-Type': 'application/json',
            'cookie': cookie,
            "bank-admin-token": bank_admin_token
        }
        return headers




    def test_params_query(self,get_hearder):
        headers = get_hearder
        url = 'https://grc-admin-sit1.test-stable.npt.maribank.io/api/dbp-grc-service/parameter/queryParameterList'
        json_data = {
            "moduleNameList":["Incident Management"]
        }
        response = requests.post(url, json=json_data, headers=headers)
        assert response.status_code == 200
        assert response.json()['data'] is not None
        print( response.json()['data'])


    def test_params_query2(self):
        self.step_login(set_param = 'step_login')
        self.step_query_param_view(set_param='step_query_param_view')

    def test_post_demo(self):
        self.step_post_demo(set_param = 'step_post_demo')

