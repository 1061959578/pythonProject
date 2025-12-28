import json
from pathlib import Path


CURRENT = Path(__file__)
BASE_DIR = CURRENT.parent.parent

class FileUtil():


    @classmethod
    def get_abspath(cls, path: str):
        return str(Path.joinpath(BASE_DIR, path))


    @classmethod
    def read_file_json(cls, path: str):
        with open(path, mode='r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                f.close()
                return data
            except Exception:
                raise Exception('Failed to read json file: %s' % path)



if __name__ == '__main__':
    CURRENT = Path(__file__)
    BASE_DIR = CURRENT.parent.parent
    print(BASE_DIR)