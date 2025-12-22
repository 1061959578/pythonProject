# conding: utf-8
# @Time : 2025/12/22下午3:33
# @Author : shiqing.duan
import requests
from Globals import Globals
from step.commom.YamlUtil import YamlUtil
from step.commom.StepPortal import StepPortal


# protocol = YamlUtil.read_conf_yaml('protocol/DBP/data_workbench_v0926/SpaceFileManagement.yml')

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


    def step_post_demo(self,set_param = None):
        headers = {
            'Content-Type': 'application/json',
            'cookie': Globals.admin_portal['cookie'],
            "bank-admin-token": Globals.admin_portal['bank-admin-token']
        }
        json_data = self.parse_param_data(set_param)
        print('解析数据')
        print(json_data)
        # json_data = {
        #     'name': 'John Doe',
        #     'age': 30,
        #     'email': 'john@example.com',
        #     'hobbies': ['reading', 'gaming']
        # }
        url = 'https://httpbin.org/post'
        response = self.call_api(url=url, method='POST', headers=headers, json=json_data)
        assert response.status_code == 200