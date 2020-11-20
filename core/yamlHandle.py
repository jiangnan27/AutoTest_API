import yaml
from config.PATH import *


class YamlHandle:
    def __init__(self, yaml_file=YAML):
        if os.path.exists(yaml_file):
            self.yaml_file = yaml_file
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    def read_data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yaml_file, 'r', encoding='utf-8') as f:
                self._data = yaml.safe_load(f)  # load后是个generator，用list组织成列表
        return self._data

    def write_data(self, content):
        with open(self.yaml_file, 'w', encoding='utf-8') as f:
            yaml.dump(content, f, allow_unicode=True, sort_keys=False)


if __name__ == '__main__':
    # yaml_handle = YamlHandle(YAML)
    # yaml_data = yaml_handle.read_data()
    # print(yaml_data)
    # yaml_data['case_suite'][0]['api_case']['login'] = '修改数据'
    # print(yaml_data)
    # yaml_handle.write_data(yaml_data)
    # new_yaml_data = yaml_handle.read_data()
    # print(new_yaml_data)
    # print(type(new_yaml_data['case_suite'][0]['api_case']['home']))
    pass
