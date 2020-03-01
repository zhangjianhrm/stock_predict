from jqdatasdk import *
import tools.PropertiesUtil as pps
import pandas as pd
from tools.MysqlUtil import MysqlInit
class JoinQuant(object):
    # 初始化自动登录
    def __init__(self):
        mypro = pps.Properties("stock.properties").getProperties()
        account = mypro["joinquant"]["account"]
        password = mypro["joinquant"]["password"]
        auth(account, password)

    # 检查是否登录
    def is_login(self):
        login = is_auth()
        if login:
            print("账户已登录")
        else:
            print("账户未登录，需要初始化JoinQuant")
        return login

    # 获取账户可以下载的条数
    def current_data_number(self):
        spare = get_query_count()["spare"]
        print("当前账户剩余可下载条数为：{}条".format(spare))
        return spare

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 100)
    myjq = JoinQuant()
    myjq.is_login()
    myjq.current_data_number()
    df=finance.run_query(
        query(finance.STK_BALANCE_SHEET).filter(finance.STK_BALANCE_SHEET.code == '000001.XSHE',
                                                finance.STK_BALANCE_SHEET.pub_date>='2019-01-01').limit(100))
    df.to_sql('STK_BALANCE_SHEET', con=MysqlInit("joinquant").get_conn(), if_exists='append', index=False)
    print(df)