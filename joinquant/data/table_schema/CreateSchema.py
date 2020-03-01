import os
import sys
import re
from tools.MysqlUtil import MysqlInit

class CreateSchema(object):
    def __init__(self):
        PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
        self.parent_path = PROJECT_ROOT + "/"

    def parse_txt(self, fileName,primaryKey,tableName,tableComment):
        f = open(self.parent_path + fileName, "r")  # 设置文件对象
        sql_fields=[]
        for line in f.readlines():
            groups=re.split(r"\t|\s", line)
            field = list(filter(None,groups))
            if field.__len__()>0:
                field_name = field[0]
                field_comment = field[1]
                field_type = field[2]
                sql_fields.append("`{}`  {} comment '{}'".format(field_name, field_type, field_comment))
        f.close()  # 关闭文件
        sql_create="create table if not exists `{}` (".format(tableName)+",".join(sql_fields)+\
                   ",primary key ({})".format(primaryKey)+" ) COMMENT '{}';".format(tableComment)
        return sql_create

def STK_BALANCE_SHEET():
    sql_create = CreateSchema().parse_txt("STK_BALANCE_SHEET.txt", "id", "STK_BALANCE_SHEET",
                                          "合并资产负债表")
    joinquantdb=MysqlInit("joinquant");
    joinquantdb.execute_sql(sql_create)
    joinquantdb.close()

if __name__ == '__main__':
   STK_BALANCE_SHEET()
