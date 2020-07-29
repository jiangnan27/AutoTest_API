import pymysql
from pymysql import OperationalError, cursors
from core.yamlReader import YamlReader
from core.my_logger import log

yaml_data = YamlReader().get_data()
host = yaml_data["db_info"]["host"]
user = yaml_data["db_info"]["user"]
password = yaml_data["db_info"]["password"]
db_name = yaml_data["db_info"]["db_name"]


class DoMysql:
    def __init__(self):
        try:  # 连接数据库
            self.connect = pymysql.connect(host=host,
                                           user=user,
                                           password=password,
                                           db=db_name,
                                           charset='utf8mb4',  # 编码格式
                                           cursorclass=cursors.DictCursor)  # 返回字典型的值
            self.cursor = self.connect.cursor()  # 建立游标
            log.info('连接数据库 - 成功。')
        except OperationalError as e:
            log.error("连接数据库 - 失败： %d: %s" % (e.args[0], e.args[1]))
        except Exception as e1:
            log.error('连接数据库 - 失败：{}'.format(e1))

    def __del__(self):  # 析构函数，实例删除时触发
        try:
            self.cursor.close()  # 先关闭游标
            self.connect.close()  # 再关闭连接
            log.info('断开数据库 - 成功。')
        except AttributeError as e:
            log.error('断开数据库 - 失败：'.format(e))

    def query_db(self, sql):
        """
        查询数据库
        :param sql:sql语句
        :return 返回一个 dict 数据
        """
        try:
            self.cursor.execute(sql)  # 执行sql语句
            result = self.cursor.fetchall()  # 获取执行的结果
            log.info('查询数据库 - 成功：{}'.format(sql))
            if len(result) == 0:
                log.info('查询数据库 - 返值：{}'.format(None))
                return None
            elif len(result) == 1:
                log.info('查询数据库 - 返值：{}'.format(result[0]))
                return result[0]
            else:
                log.info('查询数据库 - 返值：{}'.format(result))
                return None
        except Exception as e:
            log.error('查询数据库 - 失败：{}'.format(e))

    def update_db(self, sql):
        """
        更新行记录
        :param sql:sql语句
        """
        try:
            self.cursor.execute(sql)
            self.connect.commit()  # 所有对数据库有改动的操作都需要commit
            log.info('更新数据库 - 成功：{}'.format(sql))
        except Exception as e:
            log.info('更新数据库 - 失败：{}'.format(e))
            self.connect.rollback()  # 如果出了错，就需要回滚所有的操作
            log.info('-------> 回滚刚才失败的操作。')


if __name__ == '__main__':
    # d = DoMysql()
    # query_result = d.query_db('SELECT * FROM `class`;')
    # d.update_db('create table `member5` (Test INT (11) COMMENT "测试" NOT NULL) DEFAULT charset = "utf8mb4"')
    # d.update_db('insert into `member5` values (123456)')
    # query_result2 = d.query_db('SELECT * FROM `member5`;')
    # print(query_result)
    # print(type(query_result))
    # print(type(query_result[0]))
    pass
