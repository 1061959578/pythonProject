# conding: utf-8
# @Time : 2025/12/22下午5:06
# @Author : shiqing.duan
import copy

import jsonpath
import requests
from Globals import Globals


class StepPortal():

    def call_api(self,url,method,headers,json,**kwargs):
        is_json = True
        res = None
        # method = data.pop('method')
        if method.lower() == 'post':
            res = requests.post(url,headers=headers,json=json,**kwargs,timeout=60)
        elif method.lower() == 'get':
            res = requests.get(url,headers=headers,json=json,**kwargs,timeout=60)

        return res

    def parse_param_data(self,set_param):

        if set_param and not set_param.startswith("$."):
            set_param = '.'.join(['$', Globals.case_name, set_param])

        try:
            step_data = copy.deepcopy(jsonpath.jsonpath(Globals.test_data,set_param)[0])
        except:
            raise Exception('Not found %s' % set_param)
        return  copy.deepcopy(step_data)

    # 处理参考数据
