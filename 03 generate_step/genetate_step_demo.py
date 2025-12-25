# conding: utf-8
# @Time : 2025/12/25下午4:44
# @Author : shiqing.duan
import os
from string import Template

step_tmp = Template('''
    def step_${PROTOCOL}(self, selector=None):
        protocol_data, step_data = self.parse_protocol_and_data(protocol, '$.${PROTOCOL}', selector)
        res = self.call_api(step_data)
        self.update_and_assert_data(selector, res)
        return res''')


class GenerateStepDemo:
    pass

    def traversal_api_file(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_name = 'httpbin.yaml'
        file = current_dir + file_name
        with open(file, 'r',encoding='utf-8') as f:
            tmpl = Template(f.read())

        pass
    # 获取对应yaml文件的数据
    # 获取step文件模板
    # 根据对应数据生成step文件

if __name__ == '__main__':
    GenerateStepDemo().traversal_api_file()