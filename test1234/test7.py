# import pymysql
#
#
# def add():
#     conn = pymysql.connect(host='47.105.207.22', port=3306, database='school', user='jiangnan', password='xxx123...')
#     cursor = conn.cursor()
#     # cursor.execute('create table if not exists `test_title`(title varchar(10));')
#     for i in range(999, 10000):
#         cursor.execute('insert into test_title values("ha-{}")'.format(i))
#         print(i)
#     try:
#         # 提交数据
#         conn.commit()
#     except:
#         # 回滚
#         conn.rollback()
#
#
# add()


import json
import requests

url = 'http://10.88.1.39:8088//api/rgw/bucket/isExistBucket'
a = '{\'content-type\': \'application/json\', \'accessKey\': \'test\', \'SecretKey\': \'FAIL\'}'
print(type(a), a)
header = eval(a)
print(type(header), header)
param = eval("{'bucket': 111}")

result = requests.get(url=url, headers=header, params=param).json()
print(result)

