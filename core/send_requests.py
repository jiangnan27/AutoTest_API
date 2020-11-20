import unittest
import requests
import json


class BaseCse(unittest.TestCase):
    def send_requests(self, url, method, header=None, param=None, body=None, files=None):
        """
        发送接口请求
        :param url:网址
        :param method:请求方法
        :param header:请求头
        :param param: 表单数据
        :param body:json数据
        :param files:文件
        :return 返回接口的response（缩进、换行后的str）
        """
        request_file = []
        request_header = header
        request_param = param
        request_json = body
        res = dict()
        # 组装上传文件的参数
        for i in files:
            param_name = i[0]
            upload_file = i[1]
            upload_file_name = upload_file.split('/')[-1]
            param_type = i[2]
            request_file.append((param_name, (upload_file_name, open(upload_file, 'rb'), param_type)))

        # 提升容错性，转换格式
        if header is None or header == "" or header == '':
            request_header = None
        elif not isinstance(header, dict):
            request_header = json.loads(header)

        if param is None or param == "" or param == '':
            request_param = None
        elif not isinstance(param, dict):
            request_param = json.loads(param)

        try:
            # 正式发送请求
            if method.lower() == 'get':
                res = requests.get(url=url,
                                   headers=request_header,
                                   params=request_param,
                                   verify=False).json()
            elif method.lower() == 'post':
                res = requests.post(url=url,
                                    headers=request_header,
                                    data=request_param,
                                    json=request_json,
                                    files=request_file,
                                    verify=False).json()
            elif method.lower() == 'put':
                res = requests.put(url=url,
                                   headers=request_header,
                                   data=request_param,
                                   json=request_json,
                                   files=request_file,
                                   verify=False).json()
            elif method.lower() == 'delete':
                res = requests.delete(url=url,
                                      headers=request_header,
                                      data=request_param,
                                      json=request_json,
                                      files=request_file,
                                      verify=False).json()
            return json.dumps(res, indent=2, ensure_ascii=False, sort_keys=True)
        except Exception as e:
            raise Exception('{0} 接口请求失败：{1}'.format(url, e))
