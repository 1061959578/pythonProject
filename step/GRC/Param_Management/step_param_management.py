# conding: utf-8
# @Time : 2025/12/22下午3:33
# @Author : shiqing.duan
import requests
from Globals import Globals
from step.commom.StepPortal import StepPortal

class StepParamManagement(StepPortal):

    def step_query_param_view(self):
        headers = {
            'Content-Type': 'application/json',
            'cookie': Globals.admin_portal['cookie'],
            "bank-admin-token": Globals.admin_portal['bank-admin-token']
        }
        url = 'https://grc-admin-sit1.test-stable.npt.maribank.io/api/dbp-grc-service/parameter/queryParameterList'
        json_data = {
            "moduleNameList": ["Incident Management"]
        }
        response = self.call_api(url=url, method='POST', headers=headers, json=json_data)
        # response = requests.post(url, json=json_data, headers=headers)

        assert response.status_code == 200
        assert response.json()['data'] is not None
        print(response.json()['data'])
        pass