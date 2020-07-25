import logging
from config.PATH import *
import time
from utils.common import *

day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# log_dir = os.path.join(TEST_LOG, day)
log_file = os.path.join(TEST_LOG, '{}.log'.format(day))


class MyLog:
    def __init__(self, module_name):
        if os.path.exists(log_file):
            pass
        else:
            open(log_file, 'w')  # 创建测试日志文件
        self.logger = logging.getLogger(module_name)  # log收集器
        self.logger.setLevel(logging.DEBUG)  # 定义收集器的信息级别
        self.log_format = logging.Formatter(
            fmt='[%(asctime)s] %(levelname)s [%(filename)s: %(funcName)s, %(lineno)d] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')  # 定义日志的格式
        # 控制台输出日志
        self.ch = logging.StreamHandler()  # 控制台输出句柄
        self.ch.setFormatter(self.log_format)  # 控制台输出的信息格式
        self.ch.setLevel(logging.DEBUG)  # 控制台输出的信息级别

        # 文件输出日志
        self.fh = logging.FileHandler(filename=log_file, mode='a', encoding='utf-8')  # mode='a' 追加写入模式
        self.fh.setFormatter(self.log_format)  # 文件输出的信息格式
        self.fh.setLevel(logging.DEBUG)  # 文件输出的信息级别

        # 加载输出句柄
        self.logger.addHandler(self.ch)  # 把流媒体添加到控制台输出句柄内
        self.logger.addHandler(self.fh)

    def __del__(self):
        self.delete_handle()

    def get_logger(self):
        return self.logger

    def delete_handle(self):
        # 移除输出句柄,避免重复输出
        self.logger.removeHandler(self.ch)
        self.logger.removeHandler(self.fh)

        # 关闭 .log 文件，释放内存
        self.ch.close()
        self.fh.close()


my_logger = MyLog(get_module_name())
log = my_logger.get_logger()


class CaseLogModule:
    @staticmethod
    def case_log_module_request(case_id, case_name, url, method, header, data):
        """用例日志模板"""
        log.info('用例ID：{}'.format(case_id))
        log.info('用例name：{}'.format(case_name))
        log.info('请求url：{}'.format(url))
        log.info('请求method：{}'.format(method))
        log.info('请求header：{}'.format(header))
        log.info('请求data：{}'.format(data))

    @staticmethod
    def case_log_module_response(msg, response, proceed):
        if msg in str(response):
            log.info('期望结果：{}'.format(msg))
            log.info('实际结果：{}'.format(response))
        else:
            log.error('期望结果：{}'.format(msg))
            log.error('实际结果：{}'.format(response))
        # log_me1.info('结束后需要的操作：{}'.format(proceed))


if __name__ == '__main__':
    pass
    # lll = MyLog().get_logger()
    # log = lll
    # log.info('hello, this is first test of log_files')
    # log.info('hello, this is first test of log_files')
    # log.info('hello, this is first test of log_files')
