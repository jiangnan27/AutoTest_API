#! /usr/bin/python
import inspect
import os


def get_module_name():
    # last=inspect.stack()[1]
    modulePath=inspect.stack()[1][1]
    os.path.basename(modulePath)
    moduleFile=os.path.basename(modulePath)
    modulename=moduleFile.split(".")[0]
    # print("last is:",last)
    # print("modulePath:",modulePath)  # H:/AutoTest/API/my_api_autotest/utils/common.py
    # print("moduleFile:", moduleFile)  # common.py
    # print("modileName:", modulename)  # common
    return moduleFile


def get_method_name():
    # print('methodName :'+inspect.stack()[1][3])
    return inspect.stack()[1][3]


# get_module_name()
