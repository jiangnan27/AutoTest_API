import json

import requests
from utils.xml_and_json import *

headers = {
    'access-token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJ7XCJ0ZWFtSWRcIjpcIjkxYzgzNGUwMDE1OTQ3OTZhODE5NzJlYTZmYzkxNzEzXCIsXCJlbXBsb3llZUlkXCI6XCJlOGFkMGU0ZDY5NjA0MzY1OWQ0ZWQ4NzM1M2I1MTkwYVwiLFwidXNlcklkXCI6XCJkY2ViY2Q5ZTQwNGM0YTFkOTM0MTcwNDJkMjI5NWY3YVwiLFwicHJvamVjdElkXCI6XCJaWUpHMDAwMDAyXCJ9Iiwic3ViIjoi55m75b2VYWNjZXNzLXRva2VuIiwiaXNzIjoi6L27562RIiwiaWF0IjoxNTgxMzE5NjU4LCJleHAiOjE1ODEzMjcxNTh9.Xm6Rl3z1JYgLSUVPsOV7gZUZ_FBhzK2beLG6s3bkDUg'
}

request_url = 'https://www.ketangpai.com/UploadApi/editorUpload'
# 构造字典，键值对方式传参
request_data = "{\"fileTypeCode\":\"DYNAMIC_ATTACH\",\"publicRead\":\"true\"}"

img = r'H:\AutoTest\API\my_api_autotest\test_data\test_photo\testphoto.jpg'
# 上传文件单独构造成以下形式
# 'files' 上传文件的键名
# 'testphoto.jpg' 上传到服务器的文件名，可以和上传的文件名不同
# open('D:/demo.jpg') 打开的文件对象，注意文件路径正确
# 'image/jpeg' Content-Type类型
request_file = [
    ('files', ('testphoto.jpg', open(img, 'rb'), 'image/jpg',)),
    ('files', ('testphoto.jpg', open(img, 'rb'), 'image/jpg',))
]


# request_file = None
#
# print(request_file)
# print(request_data)
# print(type(request_data))
# result = requests.post(url=request_url, headers=headers, data=eval(request_data), files=request_file,
#                        verify=False).json()
# print(json.dumps(result, indent=2, ensure_ascii=False))


# url2 = 'https://m.baidu.com/'
# data = {'word': 'api',
#         'tn': '',
#         't': '1581418091326',
#         'rset': 'rcmd',
#         'rq': 'api',
#         'r': '8483',
#         'qid': '10059314241275168230',
#         'platform': 'wise',
#         'ms': '1',
#         'lsAble': '1',
#         'from': '844b',
#         'clientWidth': '918',
#         'baiduid': '468ecec7daca5139f48e999aa0714870:FG=1',
#         }
# header2 = {}
# result = requests.get(url2, params=data, headers=header2, verify=False)
#
# # result.encoding = 'utf-8'
# print(result.text)

files2 = "[(\"files\", \"H:/AutoTest/API/my_api_autotest/test_data/test_photo/testphoto.jpg\", \"image/jpeg\"),(\"files\", \"H:/AutoTest/API/my_api_autotest/test_data/test_photo/testphoto.jpg\", \"image/jpeg\")]",
data2 = "{\"fileTypeCode\": \"DYNAMIC_ATTACH\",\"publicRead\": \"true\"}"





