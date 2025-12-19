# conding: utf-8
# @Time : 2025/12/19下午4:29
# @Author : shiqing.duan
import requests


class TestParamManagement():

    def test_login(self):
        data = {
            "password":"5AEA19BDBF0350E6028DFFF43FAD46C7",
            "userId":"reviewer1"
        }
        url = 'https://grc-admin-sit1.test-stable.npt.maribank.io/api/session/credential/v1/login'
        response = requests.post(url, json=data)
        bank_admin_token = response.json()['data']
        cookies = 'token='+bank_admin_token
        headers = {}

    def test_params_query(self):

        json_data = {
            "moduleNameList":["Incident Management"]
        }