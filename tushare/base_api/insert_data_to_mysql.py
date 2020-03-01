import pandas as pd

import tushare as ts
from tools.PropertiesUtil import Properties
from tools.MysqlUtil import MysqlInit

# 股票每日交易数据入库
def daily_to_mysql():
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 100)

    tushare_properties = Properties("stock.properties").getProperties()
    tushare_token = tushare_properties["tushare"]["token"]
    ts.set_token(tushare_token)  # 设置token
    pro = ts.pro_api()
    df = pro.daily(ts_code='000001.SZ', start_date='20180718', end_date='20200227')
    print(df)
    df.to_sql('stock_daily_basic', con=MysqlInit("tushare").get_conn(), if_exists='replace', index=False)


if __name__ == "__main__":
    daily_to_mysql()