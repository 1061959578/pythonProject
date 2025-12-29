# conding: utf-8
# @Time : 2025/12/25下午4:39
# @Author : shiqing.duan
import os.path
from string import Template

from commom.FileUtil import FileUtil
from commom.YamlUtil import YamlUtil


class StepUtil(object):
    def __init__(self,apiInfo_dir = None,class_template:str = 'commom/Template/Class.template',step_template:str = 'commom/Template/Step.template'):
        '''
        :param apiInfo_dir:  api 信息文件相对路径
        :param class_template: ： 类的模板文件
        '''
        path = FileUtil.get_abspath(apiInfo_dir)
        if not os.path.exists(path):
            raise Exception('Path is not exists %s',path)
        self.apiInfo_path = path
        self.class_template = FileUtil.get_abspath(class_template)
        self.step_template = FileUtil.get_abspath(step_template)
        pass


    def traversak_apiinfo(self):
        if os.path.isfile(self.apiInfo_path):
            api_info = self.apiInfo_path
            self._generate_step(api_info)
        elif os.path.isdir(self.apiInfo_path):
            # 所过是文件夹，遍历文件夹的文件
            pass
        pass


    def _generate_step(self,api_info):
        # 定义step 路径
        step_file = api_info.replace('apiinfo','step').replace('yaml','py')
        step_dir = os.path.dirname(step_file)
        print(step_file)

        # 判断step路径存在不，不存在则创建
        os.makedirs(step_dir,exist_ok = True)

        # 获取apiInfo 的接口信息
        api_data = YamlUtil.read_conf_yaml(api_info)
        try:
        # 遍历api 接口
            for api_name in api_data.keys():
                if not os.path.exists(step_file):

                    # 获取class_template 模板文件
                    with open(self.class_template,'r',encoding='utf-8') as f_class_tmp:
                        class_tmp = Template(f_class_tmp.read())

                    # 获取对应变量值，生成文件，以及类型
                    APIINFO_FILE = api_info
                    CLASS_NAME = self.__format_string(os.path.basename(api_info)).replace('.yaml','')

                    with open(step_file,'w',encoding='utf-8') as f_step_class:
                        f_step_class.write(class_tmp.substitute(APIINFO_FILE=APIINFO_FILE,CLASS_NAME=CLASS_NAME))
                        f_step_class.write('\n')
                        f_step_class.close()

                    # 获取Step模板文件
                    with open(self.step_template,'r',encoding='utf-8') as f_step_tmp:
                        step_tmp = Template(f_step_tmp.read())
                    # 追加写入 step
                    print(api_name)
                    with open(step_file,'a',encoding='utf-8') as f_step_func:
                        f_step_func.write(step_tmp.safe_substitute(API=api_name))
                        f_step_func.write('\n')
                        f_step_func.close()

                else:
                    raise Exception('存在相关step %s',step_file)
        except Exception as e:
            raise Exception('Failed to generate step: %s' % step_file)


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