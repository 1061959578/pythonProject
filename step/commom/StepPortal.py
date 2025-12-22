# conding: utf-8
# @Time : 2025/12/22下午5:06
# @Author : shiqing.duan
import requests


class StepPortal():

    def call_api(self,url,method,headers,json,**kwargs):
        is_json = True
        res = None
        # method = data.pop('method')
        if method.lower() == 'post':
            res = requests.post(url,headers=headers,json=json,**kwargs,timeout=60)
        elif method.lower() == 'get':
            res = requests.get(url,headers=headers,json=json,**kwargs,timeout=60)

        print(res.text)

        return res