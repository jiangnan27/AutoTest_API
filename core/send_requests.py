import unittest
import requests
import json
from core.my_logger import log


class BaseCse(unittest.TestCase):
    def send_requests(self, url, method, header=None, data=None, files=None):
        """
        发送接口请求
        :param url:网址
        :param method:请求方法
        :param header:请求头
        :param data:数据体，可以是表格形式的或者json
        :param files:文件
        :return 返回接口的response（缩进、换行后的str）
        """
        try:
            # res = None
            request_file = []
            request_header = header
            request_data = data
            # 组装上传文件的参数
            if files is None or files == "" or files == '':
                pass
            else:
                if isinstance(files, str):  # 提升输入格式的容错
                    files = eval(files)
                elif isinstance(files, list):
                    files = files
                for i in files:
                    param_name = i[0]
                    upload_file = i[1]
                    upload_file_name = upload_file.split('/')[-1]
                    param_type = i[2]
                    request_file.append((param_name, (upload_file_name, open(upload_file, 'rb'), param_type)))

            # 提升容错性，转换格式
            if header is None or header == "" or header == '':
                request_header = None
            elif isinstance(header, dict):
                pass
            else:
                request_header = json.loads(header)

            # 正式发送请求
            if method.lower() == 'get':
                res = requests.get(url=url,
                                   headers=request_header,
                                   params=request_data.encode("utf-8"),
                                   files=request_file,
                                   verify=False).json()
            elif method.lower() == 'post' and len(request_file) == 0:
                res = requests.post(url=url,
                                    headers=request_header,
                                    data=json.dumps(request_data).encode("utf-8"),
                                    files=request_file,
                                    verify=False).json()
            elif method.lower() == 'post' and len(request_file) > 0:
                res = requests.post(url=url,
                                    headers=request_header,
                                    data=request_data,
                                    files=request_file,
                                    verify=False).json()
            else:
                log.error('目前只支持 get、post 两种请求方式。')
                self.fail('目前只支持 get、post 两种请求方式。')
            return json.dumps(res, indent=2, ensure_ascii=False, sort_keys=True)
        except Exception as e:
            log.error('{0} 接口请求失败：{1}'.format(url, e))
            raise Exception
