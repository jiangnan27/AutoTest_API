import copy

a = [{
    "csv_loop": "login.xlsx\\login",
    "case_id": "home_001",
    "case_name": "my_get_csv(\"case_name\")",
    "url": "https://mobile-test.qingzhuyun.com/api/mobile/login",
    "method": "post",
    "header": "{\"content-type\": \"application/json\"}",
    "data": "{\"userName\":my_get_csv(\"userName\"),\"password\": my_get_csv(\"password\")}",
    "sql": "",
    "msg": "成功",
    "result": "PASS",
    "proceed": "[my_setattr(\"access-token\",response[\"data\"][\"access-token\"]),my_setattr(\"userId\",response[\"data\"][\"userId\"])]",
    "tester": "mua~222"
  }]

csv_case_data_lists = [{'case_name': '正常登录', 'userName': '13290021660', 'password': 'e10adc3949ba59abbe56e057f20f883e'},
     {'case_name': '错误用户名登录', 'userName': '1329002166', 'password': 'e10adc3949ba59abbe56e057f20f883e'},
     {'case_name': '错误密码登录', 'userName': '13290021660', 'password': '123546'},
     {'case_name': '空用户名登录', 'userName': '', 'password': 'e10adc3949ba59abbe56e057f20f883e'},
     {'case_name': '空密码登录', 'userName': '13290021660', 'password': ''}]

base_index = 0


copy_data = copy.deepcopy(a[0])  # ######################
# print(copy_data)

new_copy_data = {}

for csv_index, csv_data_dict in enumerate(csv_case_data_lists):
    for k, v in copy_data.items():
        def my_get_csv(name: str, csv_data_dict777=None):
            if csv_data_dict777 is None:
                result = csv_data_dict[name]
                return result  # ################  一结束，a就变了  ########################
        # print('此时v：', v)
        if 'my_get_csv' in str(v):
            result2 = eval(v)  # ###############################################
            new_copy_data[k] = result2
        else:
            new_copy_data[k] = v
    # print('此时new_copy_data：', new_copy_data)

    if csv_index == 0:
        insert_index1 = base_index
        a[insert_index1] = copy.deepcopy(new_copy_data)  # 修改 raw_case_data
    else:
        insert_index2 = base_index + csv_index
        print('插入a{} = {}'.format(insert_index2, new_copy_data))
        a.insert(insert_index2, copy.deepcopy(new_copy_data))  # 把这条修改过的 数据 加入 raw_case_data



print(a)
