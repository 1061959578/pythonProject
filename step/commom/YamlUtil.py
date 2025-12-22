

from step.commom.FileUtil import FileUtil


class YamlUtil():

    @classmethod
    def read_conf_yaml(cls, path: str):
        """
        Read file content
        :param path: file path - relative to root directory
        :return: file content
        """
        # real_path = FileUtil.get_abspath(path)
        # with open(real_path, mode='r', encoding='utf-8') as f:
        #     if f is None:
        #         # raise OpenFileException(real_path
        #         raise Exception
        #     data = yaml.load(stream=f, Loader=yaml.FullLoader)
        #     f.close()
        #     return data
    pass