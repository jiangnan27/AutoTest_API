import copy
import json
from core.do_excel import DoExcel
from config.PATH import *
from core.yamlReader import YamlReader
from core.my_logger import log
from utils.common import *


base_case_filename = os.path.join(BASE_CASE_DATA, "api_case.xlsx")
yaml_data = YamlReader().get_data()
mode = yaml_data["case_suite"]


class GetCaseData:
    @staticmethod
    def __csv_update_to_raw(raw_data, csv_data):
        """把 csv 的数据 替换进入 raw_case_data"""
        aa = copy.deepcopy(raw_data)
        bb = copy.deepcopy(csv_data)
        new_data = {}  # csv的单条用例
        new_data_list = []  # csv的所有用例

        for csv_index, csv_data_dict in enumerate(bb):  # 更新所有csv
            def get_csv(name: str, csv_data_dict777=None):  # 内置函数，更新单条csv的时候能够用到
                if csv_data_dict777 is None:
                    csv_result = csv_data_dict[name]
                    return csv_result

            for base_k, base_v in aa.items():  # 更新单条csv
                if "get_csv" in str(base_v):
                    new_data[base_k] = eval(base_v)
                elif base_k in csv_data_dict.keys() and csv_data_dict[base_k] != base_v:
                    new_data[base_k] = csv_data_dict[base_k]
                else:
                    new_data[base_k] = base_v

            new_data_list.append(copy.deepcopy(new_data))  # 把单条csv用例放入一个list
        return new_data_list

    def get_case_data(self):
        a = []
        for sheet_name, case_order in mode.items():  # 读取所有的原始数据
            data = DoExcel(base_case_filename, sheet_name).read_excel(case_order)
            for i in data:  # 把表的名字加进去，为后面写入用例结果和用例时间做准备
                i["sheet_name"] = sheet_name
            for i in data:  # 放进一个新的列表
                a.append(i)

        old_case_data = copy.deepcopy(a)  # 深度copy，不会影响最原始的数据
        # print(old_case_data)
        new_case_data = []
        for old_data_01 in old_case_data:
            # print(old_data_01)
            if "get_csv" in str(old_data_01):  # 看看是不是需要开启csv参数化
                csv_data_filepath = os.path.join(CSV_CASE_DATA, old_data_01["csv_loop"].split("/")[0])
                csv_data_sheet_name = old_data_01["csv_loop"].split("/")[1]
                # print(csv_data_filepath)
                # print(csv_data_sheet_name)
                csv_case_data = DoExcel(csv_data_filepath, csv_data_sheet_name).read_excel()
                # print(csv_case_data)
                new_data_list = self.__csv_update_to_raw(old_data_01, csv_case_data)
                for i in new_data_list:
                    new_case_data.append(i)
            else:
                new_case_data.append(old_data_01)

        # 重构case_id，在原始的case_id前面加上序号
        for data_idx, data_value in enumerate(new_case_data):
            old_case_id = data_value["case_id"]
            new_case_id = str("%04d" % (data_idx + 1)) + "_" + old_case_id
            new_case_data[data_idx]["case_id"] = new_case_id
        log.info("获取到的用例数据：{}".format(json.dumps(new_case_data, ensure_ascii=False, indent=2)))
        # print("获取到的用例数据：{}".format(json.dumps(new_case_data, ensure_ascii=False, indent=2)))
        # print("获取到的用例数据：{}".format(eval(json.dumps(new_case_data, ensure_ascii=True, indent=2))))
        return new_case_data
