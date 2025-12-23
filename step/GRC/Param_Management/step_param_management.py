# conding: utf-8
# @Time : 2025/12/22下午3:33
# @Author : shiqing.duan
import requests
from Globals import Globals
from step.commom.YamlUtil import YamlUtil
from step.commom.StepPortal import StepPortal


# protocol = YamlUtil.read_conf_yaml('protocol/DBP/data_workbench_v0926/SpaceFileManagement.yml')

class StepParamManagement(StepPortal):

    def step_query_param_view(self,set_param = None):
        headers = {
            'Content-Type': 'application/json',
            'cookie': Globals.admin_portal['cookie'],
            "bank-admin-token": Globals.admin_portal['bank-admin-token']
        }
        url = 'https://grc-admin-sit1.test-stable.npt.maribank.io/api/dbp-grc-service/parameter/queryParameterList'
        json_data = self.parse_param_data(set_param)
        # json_data = {
        #     "moduleNameList": ["Incident Management"]
        # }
        response = self.call_api(url=url, method='POST', headers=headers, json=json_data)
        print(response.text)
        assert response.status_code == 200
        assert response.json()['data'] is not None



    def step_post_demo(self,set_param = None):
        headers = {
            'Content-Type': 'application/json',
            'cookie': Globals.admin_portal['cookie'],
            "bank-admin-token": Globals.admin_portal['bank-admin-token']
        }
        json_data = self.parse_param_data(set_param)
        url = 'https://httpbin.org/post'
        response = self.call_api(url=url, method='POST', headers=headers, json=json_data)
        print(response.json())
        assert response.status_code == 200