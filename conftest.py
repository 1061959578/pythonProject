import copy
import os

import pytest

from Globals import Globals
from step.commom.FileUtil import FileUtil
from step.commom.YamlUtil import YamlUtil


def pytest_runtest_call(item):
    Globals.case_path = item.path
    Globals.case_name = item.originalname


@pytest.fixture(scope='module',autouse=True)
def get_case_data(request):

    # 通过node 获取文件相对路径，并找到对应yaml配置文件
    node_id = request.node.nodeid
    case_path = node_id.split('::')[0]
    yaml_path = case_path.replace('.py', '.yaml')
    print('case_path', case_path)

    # 判断文件存在，获取文件数据
    if os.path.exists(FileUtil.get_abspath(yaml_path)):
        Globals.test_data = YamlUtil.read_conf_yaml(yaml_path)
    else:
        raise Exception('File path: %s is not exist!' % yaml_path)

    Globals.case_data = copy.deepcopy(Globals.test_data)




