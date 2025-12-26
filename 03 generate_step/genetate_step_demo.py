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
        # 获取模板文件
        current_dir = os.path.dirname(os.path.realpath(__file__))
        template_file = current_dir + '\\' + 'Step.template'
        with open(template_file, 'r',encoding='utf-8') as f_tp:
            tmpl = Template(f_tp.read())
            f_tp.close()

        # 生成step
        file_name = 'httpbin.yaml'
        step_file = 'Step_demo.py'


        with open(step_file, 'a',encoding='utf-8') as f_step:
            lines = f_step.write(tmpl.substitute(PROTOCOL_PATH=file_name,CLASS_NAME=file_name.replace('.yaml','')))
            f_step.close()
        pass


    # 获取对应yaml文件的数据
    # 获取对应yaml文件的数据
    # 获取step文件模板
    # 根据对应数据生成step文件

if __name__ == '__main__':
    GenerateStepDemo().traversal_api_file()