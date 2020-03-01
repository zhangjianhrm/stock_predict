create database if not exists stock_tushare DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use stock_tushare;

-- select * from stock_tushare.stock_daily_basic;

create table if not exists stock_daily_basic(
ts_code  varchar(20) comment 'TS股票代码',
trade_date date  comment '交易日期',
`open` float comment '开盘价',
high float comment '最高价',
low float comment '最低价',
`close` float comment '收盘价',
pre_close float comment '昨收价',
`change` float comment '涨跌额',
pct_chg float comment '涨跌幅',
vol float comment '成交量(手)',
amount float comment '成交额(千万)',
primary key (ts_code,trade_date) comment '股票和日期联合主键'
) COMMENT '全部股票每日重要的基本面指标';

