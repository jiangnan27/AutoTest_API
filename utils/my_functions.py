#! /usr/bin/python
import hashlib
import random
import re
import time


class __AddValue:
    """
    反射机制
    用来设置用例用的全局变量
    """
    var = None


def my_setattr(attr_name: str, attr_value):
    """
    设置全局变量
    :param attr_name:全局变量名
    :param attr_value: 全局变量值
    """
    setattr(__AddValue, attr_name, attr_value)


def my_getattr(attr_name: str):
    """
    引用全局变量
    :param attr_name: 全局变量名
    :return: 全局变量值
    """
    result = getattr(__AddValue, attr_name)
    return result


def my_hasattr(attr_name: str):
    """
    判断是否有全局变量
    :param attr_name: 全局变量名
    :return: bool值
    """
    result = hasattr(__AddValue, attr_name)
    return result


def my_delattr(attr_name: str):
    """
    删除全局变量
    :param attr_name: 全局变量名
    """
    delattr(__AddValue, attr_name)


def my_randint(min_int: int, max_int: int):
    """
    随机整数
    :param min_int: 区间的最小值
    :param max_int: 区间的最大值
    :return: 一个int
    """
    random_result = random.randint(min_int, max_int)
    return random_result


def my_now_time(time_format=None):
    """
    获取现在的时间
    :param time_format: 时间的格式
    """
    if time_format is None:  # 默认格式
        time_format = '%Y-%m-%d %H:%M:%S'
    return time.strftime(time_format, time.localtime(time.time()))


def my_md5(text):
    """MD5加密"""
    m1 = hashlib.md5()
    m1.update(text.encode('utf-8'))
    md5_str = m1.hexdigest()
    return md5_str


def my_remove_spaces(text):
    """祛除所有空格"""
    pattern = re.compile(r'\s+')
    return re.sub(pattern, "", text)


