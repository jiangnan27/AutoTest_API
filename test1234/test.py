import json
import requests

# request_header = {
#     'Content-Type': 'application/json',
#     'access-token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJ7XCJ0ZWFtSWRcIjpcIjkxYzgzNGUwMDE1OTQ3OTZhODE5NzJlYTZmYzkxNzEzXCIsXCJlbXBsb3llZUlkXCI6XCJlOGFkMGU0ZDY5NjA0MzY1OWQ0ZWQ4NzM1M2I1MTkwYVwiLFwidXNlcklkXCI6XCJkY2ViY2Q5ZTQwNGM0YTFkOTM0MTcwNDJkMjI5NWY3YVwiLFwicHJvamVjdElkXCI6XCJaWUpHMDAwMDAyXCJ9Iiwic3ViIjoi55m75b2VYWNjZXNzLXRva2VuIiwiaXNzIjoi6L27562RIiwiaWF0IjoxNTgxMzE5NjU4LCJleHAiOjE1ODEzMjcxNTh9.Xm6Rl3z1JYgLSUVPsOV7gZUZ_FBhzK2beLG6s3bkDUg'
# }

# request_header = None
#
# request_url = 'https://www.ketangpai.com/UploadApi/editorUpload'
# # 构造字典，键值对方式传参
# request_data = "{\"fileTypeCode\":\"DYNAMIC_ATTACH\",\"publicRead\":\"true\", \"body\": \"哈哈\"}"
#
# img1 = r'D:\study\other\AutoTest_API\test_data\upload_file\testphoto.jpg'
# img2 = r'D:\study\other\AutoTest_API\test_data\upload_file\20191012143430.jpg'

# 上传文件单独构造成以下形式
# 'files' 上传文件的键名
# 'testphoto.jpg' 上传到服务器的文件名，可以和上传的文件名不同
# open('D:/demo.jpg') 打开的文件对象，注意文件路径正确
# 'image/jpeg' Content-Type类型
# request_file = (
#     ('files', ('testphoto.jpg', open(img1, 'rb'), 'image/jpg',)),
#     ('files', ('testphoto.jpg', open(img2, 'rb'), 'image/jpg',))
# )
#
#
# # request_file = None
# print("request_header: ", request_header)
# print("request_file: ", request_file)
# print("request_data: ", request_data, type(request_data))
# result = requests.post(url=request_url, headers=request_header, data=json.loads(request_data.encode("utf-8")), files=request_file,
#                        ).json()
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

# method = 'post'


url0 = "http://47.105.207.22/prod-api/captchaImage"
header0 = ''
data0 = ""
print(header0)
print(data0)
response0 = requests.get(url=url0, headers=header0, params=data0).json()
print(response0)

uuid = response0["uuid"]

url = 'http://47.105.207.22/prod-api/login'
# header = {'content-type': 'application/json'}
header = {'content-type': 'application/json',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
# header = ""
data = {"username": "admin", "password": "admin123", "uuid": uuid}

data = json.dumps(data)
# data = json.loads(data)

header = json.loads(json.dumps(header))

print(header)
print(data)

response = requests.post(url=url, headers=header, data=data).json()
print(json.dumps(response, ensure_ascii=False, indent=2))

# token = response["token"]
# url2 = 'http://47.105.207.22/prod-api/system/user/profile/avatar'
# header2 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
#            "Authorization": token}
# Cookie = {"Cookie": "Admin-Token=" + token}
# data2 = json.dumps({"Cookie": "Admin-Token=" + token})
# img3 = r'D:\study\other\AutoTest_API\test_data\upload_file\20191012143430.jpg'
# files = (
#     ('avatarfile', ('blob', open(img3, 'rb'), 'image/jpg',)),
# )
# response2 = requests.post(url=url2, headers=header2, cookies=Cookie, data=data2, files=files).json()
#
# print(header2)
# print(data2)
# print(json.dumps(response2, ensure_ascii=False, indent=2))
