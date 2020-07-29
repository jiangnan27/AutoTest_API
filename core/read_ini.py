import configparser


class ReadIni:
    @staticmethod
    def get_ini_value(file_name, section, option):
        """读取  ini  文件"""
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf[section][option]


if __name__ == '__main__':
    # filepath = r'H:\AutoFramework_Own\API\my_api_autotest\config\case.ini'
    # r = eval(ReadIni.get_ini_value(filepath, 'MODE', 'mode'))
    # print(r)
    # # print(type(r))
    # # print(type(r['login']))
    # for k, v in r.items():
    #     k1 = k
    #     v1 = v
    #     print(k1)
    #     # print(type(k1))
    #     # print(v1)
    #     # print(type(v))
    pass
