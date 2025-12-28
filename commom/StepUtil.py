# conding: utf-8
# @Time : 2025/12/25下午4:39
# @Author : shiqing.duan
import os.path

from commom.FileUtil import FileUtil
from commom.YamlUtil import YamlUtil


class StepUtil(object):
    def __init__(self,apiInfo_dir = None,class_template:str = 'Class.template'):
        '''
        :param apiInfo_dir:  api 信息文件相对路径
        :param class_template: ： 类的模板文件
        '''
        path = FileUtil.get_abspath(apiInfo_dir)
        if not os.path.exists(path):
            raise Exception('Path is not exists %s',path)
        self.apiInfo_path = path
        pass


    def traversak_apiinfo(self):
        if os.path.isfile(self.apiInfo_path):
            api_info = self.apiInfo_path
            self._generate_step(api_info)
        pass


    def _generate_step(self,api_info):
        print(api_info)
        # 定义step 路径
        step_file = api_info.replace('apiInfo','step').replace('yaml','py')
        step_dir = os.path.dirname(step_file)
        class_name = self.__format_string(os.pathbasename(step_file))

        # 判断step路径存在不，不存在则创建
        os.makedirs(step_dir,exist_ok = True)

        # 获取apiInfo 的接口信息
        api_data = YamlUtil.read_conf_yaml(api_info)
        # 遍历api 接口
        for api_name in api_data.keys():
            if not os.path.exists(step_file):
                pass
            else:
                raise Exception('存在相关step %s',step_file)


    def __format_string(self, value=None):
        set_null = ' ,。，*!@#¥%&()（）、/\\'

        for i in range(len(set_null)):
            if set_null[i] in value:
                value = value.replace(set_null[i], '')

        value = value.replace('.py', '')
        value = value.replace('-', '_')

        return value



if __name__ == '__main__':
    api_info = 'apiinfo/httpbin.yaml'
    StepUtil('apiinfo/httpbin.yaml').traversak_apiinfo()
    pass