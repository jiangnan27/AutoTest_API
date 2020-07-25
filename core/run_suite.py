<<<<<<< HEAD
from core.my_logger import *
=======
from core.my_log import *
>>>>>>> origin/master
import time
import unittest
from HTMLTestRunnerCN import HTMLTestRunner
from config.PATH import *

now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
dir_report = os.path.join(TEST_REPORT, day)
test_case_path = TEST_CASE

suite = unittest.defaultTestLoader.discover(test_case_path, 'test*.py')


def run_suite():
    filename = dir_report + "\\" + now + "_result.html"

    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='接口自动化测试报告',
                            description='执行情况：')
    runner.run(suite)
    fp.close()  # 关闭报告文件


if os.path.exists(dir_report):
    run_suite()
else:
    os.mkdir(dir_report)  # 创建测试日志文件夹
    run_suite()


