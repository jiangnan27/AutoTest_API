import json
import unittest
import openpyxl
import urllib3
from config.PATH import *
import ddt
from core.do_excel import DoExcel
from core.send_requests import BaseCse
<<<<<<< HEAD:test_case/test_api_demo.py
from core.my_logger import CaseLogModule
from core.my_logger import MyLog
=======
from core.my_log import CaseLogModule
from core.my_log import log
>>>>>>> origin/master:test_case/test_api.py
from utils.my_functions import *
from utils.get_case_data import GetCaseData
from utils.common import *


# 获取原始用例数据 和 CSV的参数化用例数据，并且合并成最终的用例数据。
new_case_data = GetCaseData().get_case_data()

test_result = None


@ddt.ddt
class TestApiDemo(BaseCse):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        log .info('')
        log .info('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  用例开始  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    @ddt.data(*new_case_data)
    def test_api_case(self, data1):
<<<<<<< HEAD:test_case/test_api_demo.py
=======
        # 分割用例数据
        # 用例结果
        global test_result

        # 用例请求头
        if data1['header'] != "":
            header = json.loads(json.dumps(eval(data1['header'])))
        else:
            header = None

        # 用例名字
        case_name = data1['case_name']

        # 用例id
        case_id = data1['case_id']

        # 接口url
        url = data1['url']

        # 接口method
        if isinstance(data1['method'], dict):
            method = json.dumps(data1['method'])
        else:
            method = data1['method']

        # 接口data - 没调用内置函数版本
        if isinstance(data1['data'], dict) or isinstance(data1['data'], list) or isinstance(data1['data'], tuple):
            data = json.dumps(data1['data'])
        else:
            data = data1['data']

        # 接口data - 要调用内置函数版本
        if 'my_' in str(data):
            new_data = json.dumps(eval(data))
        else:
            new_data = data

        # 接口data - 文件
        if data1['files'] == "":
            files = None
        elif data1['files'] != "" and isinstance(data1['files'], str):
            files = eval(data1['files'])
        else:
            files = data1['files']

        # 期望结果
        msg = data1['msg']

        # 后续操作
        if isinstance(data1['proceed'], dict) or isinstance(data1['proceed'], list) or isinstance(data1['proceed'], tuple):
            proceed = json.dumps(eval(data1['proceed']))
        else:
            proceed = data1['proceed']

        # 打印日志
        CaseLogModule.case_log_module_request(case_id, case_name, url, method, header, new_data)
        print('用例ID：{}'.format(case_id))
        print('用例name：{}'.format(case_name))
        print('请求url：{}'.format(url))
        print('请求method：{}'.format(method))
        print('请求header：{}'.format(header))
        print('请求data：{}'.format(new_data))

        # 发送请求
        response = json.loads(self.send_requests(url, method, header, new_data, files))

        # 打印日志
        CaseLogModule.case_log_module_response(msg, response, proceed)
        print('期望结果：{}'.format(msg))
        print('实际结果：{}'.format(response))

        # 执行后续操作
        if proceed != "":
            log .info('添加全局变量：{}'.format(proceed))
            eval(proceed)

>>>>>>> origin/master:test_case/test_api.py
        try:
            # 分割用例数据
            global test_result
            if data1['header'] != "":
                header = json.loads(json.dumps(eval(data1['header'])))
            else:
                header = None
            case_name = data1['case_name']
            case_id = data1['case_id']
            url = data1['url']
            if isinstance(data1['method'], dict):
                method = json.dumps(data1['method'])
            else:
                method = data1['method']

            if isinstance(data1['data'], dict) or isinstance(data1['data'], list) or isinstance(data1['data'], tuple):
                data = json.dumps(data1['data'])
            else:
                data = data1['data']

            if 'my_' in str(data):
                new_data = json.dumps(eval(data))
            else:
                new_data = data

            if data1['files'] == "":
                files = None
            elif data1['files'] != "" and isinstance(data1['files'], str):
                files = eval(data1['files'])
            else:
                files = data1['files']

            msg = data1['msg']

            if isinstance(data1['proceed'], dict) or isinstance(data1['proceed'], list) or isinstance(data1['proceed'], tuple):
                proceed = json.dumps(eval(data1['proceed']))
            else:
                proceed = data1['proceed']

            # 打印日志
            CaseLogModule.case_log_module_request(case_id, case_name, url, method, header, new_data)
            print('用例ID：{}'.format(case_id))
            print('用例name：{}'.format(case_name))
            print('请求url：{}'.format(url))
            print('请求method：{}'.format(method))
            print('请求header：{}'.format(header))
            print('请求data：{}'.format(data))

            # 发送请求
            response = json.loads(self.send_requests(url, method, header, new_data, files))

            # 打印日志
            CaseLogModule.case_log_module_response(msg, response, proceed)
            print('期望结果：{}'.format(msg))
            print('实际结果：{}'.format(response))

            # 添加变量，为下一个接口做准备
            if proceed != "":
                log_me456 .info('添加全局变量：{}'.format(proceed))
                eval(proceed)

            # 断言
            self.assertIn(msg, json.dumps(response, ensure_ascii=False))
            test_result = 'PASS'
        except AssertionError as e:
            test_result = 'FAIL'
            log.error(e)
            raise e
        finally:
            log.info('-----------------------------> 对Excel写入测试结果 <-----------------------------')
            base_case_filename = os.path.join(BASE_CASE_DATA, 'api_case.xlsx')
            identify = data1['sheet_name'] + data1['csv_loop']

            # 统计csv的数量，来决定 被输入行数 是否需要再增加
            if new_case_data.index(data1) == 0 and data1['csv_loop'] != "":
                my_setattr('csv_count', 1)
            elif new_case_data.index(data1) == 0:
                my_setattr('csv_count', 0)
            # 新的csv_name不能是"" + 老的csv_name不能是"" + 新的csv_name != 老的csv_name。这样才算是真正的多了一条参数化用例数据。
            elif data1['csv_loop'] != "" and my_getattr('csv_name') != "" and data1['csv_loop'] != my_getattr('csv_name'):
                my_setattr('csv_count', my_getattr('csv_count') + 1)

            # 初始化 - 被输入的行数（列数是固定的位置，不用初始化）
            # 只要文件名、表名任何一个名字不再相同，就会进行 初始化
            if new_case_data.index(data1) == 0 or identify != my_getattr('identify'):
                my_setattr('base_row_n', 2)
                my_setattr('csv_row_n', 2)
                my_setattr('identify', identify)
            else:
                my_setattr('identify', identify)

            if data1['csv_loop'] != "":  # 对csv用例文件写入结果
                csv_result_filepath = os.path.join(CSV_CASE_DATA, data1['csv_loop'].split('/')[0])
                csv_result_sheet_name = data1['csv_loop'].split('/')[1]
                excel = openpyxl.load_workbook(csv_result_filepath)
                table = excel[csv_result_sheet_name]
                max_col = table.max_column
                # 写入结果
                DoExcel(csv_result_filepath, csv_result_sheet_name).write_excel(
                                                         test_result,
                                                         my_getattr('csv_row_n'),
                                                         max_col-2)
                # 写入测试时间
                DoExcel(csv_result_filepath, csv_result_sheet_name).write_excel(
                                                         my_now_time(),
                                                         my_getattr('csv_row_n'),
                                                         max_col)
                my_setattr('csv_row_n', my_getattr('csv_row_n')+1)  # 加一行
            else:  # 对base用例文件写入结果
                excel = openpyxl.load_workbook(base_case_filename)
                table = excel[data1['sheet_name']]
                max_col = table.max_column
                # 写入结果
                DoExcel(base_case_filename, data1['sheet_name']).write_excel(
                                                        test_result,
                                                        my_getattr('csv_count') + my_getattr('base_row_n'),
                                                        max_col-3)
                # 写入测试时间
                DoExcel(base_case_filename, data1['sheet_name']).write_excel(
                                                        my_now_time(),
                                                        my_getattr('csv_count') + my_getattr('base_row_n'),
                                                        max_col)
                my_setattr('base_row_n', my_getattr('base_row_n')+1)  # 加一行

            # 老的csv_name：把csv_loop设置成全局变量，为下一条的  统计csv数量  做准备
            my_setattr('csv_name', data1['csv_loop'])

    def tearDown(self):
        log .info('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  用例结束  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        log .info('')


if __name__ == '__main__':
    unittest.main()
