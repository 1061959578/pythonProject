import os

import pytest

from Globals import Globals


def pytest_runtest_call(item):
    Globals.case_path = item.path
    Globals.case_name = item.originalname


@pytest.fixture(scope='moudule',autouse=True)
def get_case_data(requset):
    node_id = request.node.nodeid

    case_path = node_id.split('::')[0]
    yaml_path = case_path.replace('.py', '.yml')

    # If data exist in yaml file
    if os.path.exists(FileUtil.get_abspath(yaml_path)):
        Globals.test_data = YamlUtil.read_conf_yaml(yaml_path)
    else:
        # If data exist in json file
        json_path = yaml_path.replace('.yml', '.json')
        if not os.path.exists(FileUtil.get_abspath(json_path)):
            raise Exception('File path: %s is not exist!' % json_path)

        Globals.test_data = FileUtil.read_file_json(FileUtil.get_abspath(json_path))

    Globals.case_data = copy.deepcopy(Globals.test_data)
    pass