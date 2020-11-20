import sys
import os

sys.path.append(os.getcwd())

import time
import unittest
from HTMLTestRunnerCN import HTMLTestRunner
from config.PATH import *
from core.my_logger import log
from core.yamlHandle import YamlHandle


def run_case(command):
    """修改yaml中的case_suite"""
    yaml_handle = YamlHandle(YAML)
    yaml_data = yaml_handle.read_data()  # 读取yaml
    for index, i in enumerate(command):
        command_list = i.split(':')
        if len(command_list) != 0:
            case_file = command_list[0]
            case_table = command_list[1]
            case_order = command_list[2]
            # 按输入的指令修改yaml内容
            # 一定需要一步一步来，不然完全更改旧的yaml数据
            yaml_data['case_suite'] = list()
            yaml_data['case_suite'].append({case_file: dict()})
            yaml_data['case_suite'][index][case_file] = {case_table: case_order}

    yaml_handle.write_data(yaml_data)  # 写入yaml


def run_suite():
    # 命令形式1 = 全部行的用例 = python run_suite.py api_case.xlsx:login:all
    # 命令形式2 = 指定行的用例 = python run_suite.py api_case.xlsx:login:2,5,7
    # 命令形式3 = 某一部的用例 = python run_suite.py api_case.xlsx:login:2-9
    custom_run_command = sys.argv[1:]  # 获取外部指令
    if len(custom_run_command) != 0:  # 如果没输入指令就不执行操作
        run_case(custom_run_command)  # 执行之前先修改yaml内容，自定义调整需要执行的用例

    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))  # 当前时间（命名报告文件）
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 今天日期（命名报告目录）
    dir_report = os.path.join(TEST_REPORT, day)  # 报告目录

    suite = unittest.defaultTestLoader.discover(TEST_CASE, 'test*.py')  # 测试套件

    if not os.path.exists(dir_report):  # 如果没有报告文件夹，就创建
        os.mkdir(dir_report)
    elif len(os.listdir(TEST_REPORT)) > 60:  # 防止报告文件过多，只保存两个月的报告
        os.rmdir(os.listdir(TEST_REPORT)[0])

    filename = os.path.join(dir_report, now + "_result.html")  # 报告文件

    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='接口自动化测试报告',
                            custom_logger=log,
                            description='执行情况：')
    runner.run(suite)
    fp.close()  # 关闭报告文件


if __name__ == "__main__":
    run_suite()
