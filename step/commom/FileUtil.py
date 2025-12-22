from pathlib import Path


CURRENT = Path(__file__)
BASE_DIR = CURRENT.parent.parent.parent

class FileUtil():


    @classmethod
    def get_abspath(cls, path: str):
        return str(Path.joinpath(BASE_DIR, path))


    pass

if __name__ == '__main__':
    CURRENT = Path(__file__)
    BASE_DIR = CURRENT.parent.parent.parent
    print(BASE_DIR)