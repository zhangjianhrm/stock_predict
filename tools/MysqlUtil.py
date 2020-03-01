from tools.PropertiesUtil import Properties
import pymysql
pymysql.install_as_MySQLdb()  # 为了兼容mysqldb
from sqlalchemy import create_engine

class MysqlInit(object):

    def __init__(self,databaseName):
        tushare_properties = Properties("stock.properties").getProperties()
        account=tushare_properties["mysql"]["account"]
        password=tushare_properties["mysql"]["password"]
        ip=tushare_properties["mysql"]["ip"]
        port=int(tushare_properties["mysql"]["port"])
        database=tushare_properties["mysql"]["database"][databaseName]
        self.conn = create_engine(
            "mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(account, password, ip, port, database))
        self.pyconn = pymysql.connect(host=ip, port=port, user=account, passwd=password, db=database,
                               charset='utf8')

    def get_conn(self):
        return self.conn

    def close(self):
        self.pyconn.close()

    def execute_sql(self,sql):
        cursor = self.pyconn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor