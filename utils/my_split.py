from utils.my_functions import *


def my_split(resource_data: str, split_content: dict):
    """
    :param resource_data: 被替换的原数据
    :param split_content: 需要替换的内容
    """
    matches = re.findall(r"(?<=\$\{).*?(?=\})", resource_data)  # 提取需要替换的目标

    new_data = None  # 替换后的数据
    for i in matches:  # 替换过程
        new_value = split_content[i]
        if i == matches[0]:
            new_data = resource_data.replace("${" + i + "}", str(new_value))
        else:
            new_data = new_data.replace("${" + i + "}", str(new_value))
    return new_data


def get_str(resource_str: str, start_str: str = "\$\{", end_str: str = "\}"):
    return re.findall(r"(?<={0}).*?(?={1})".format(start_str, end_str), resource_str)  # 提取需要替换的目标


def deal_function_data(resource_data: str):
    """处理测试数据中的函数"""
    if isinstance(resource_data, str):
        resource_data = resource_data
    else:
        # resource_data = json.dumps(resource_data, ensure_ascii=False)
        resource_data = str(resource_data)

    if r"${my_" in resource_data:
        matches = get_str(resource_data, "\$\{", "\}")
        new_data = None  # 替换后的数据
        for i in matches:  # 替换过程
            result = eval(str(i))
            check = resource_data.split("${" + i + "}")
            if isinstance(result, str) and check[0][-1] not in ["\'", "\""] and check[1][0] not in ["\'", "\""]:
                new_value = '\"' + result + '\"'
            else:
                new_value = result

            if i == matches[0]:
                new_data = resource_data.replace("${" + i + "}", str(new_value))
            else:
                new_data = new_data.replace("${" + i + "}", str(new_value))
    else:
        new_data = resource_data
    return new_data
