import yaml
from config.PATH import *


class YamlReader:
    def __init__(self, yaml_file=YAML):
        if os.path.exists(yaml_file):
            self.yaml_file = yaml_file
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    # @property
    def get_data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yaml_file, 'rb') as f:
                self._data = yaml.unsafe_load(f)  # load后是个generator，用list组织成列表
        return self._data


if __name__ == '__main__':
    # read = YamlReader(YAML)
    # result = read.get_data()
    pass
