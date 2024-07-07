from datetime import datetime
import akshare as ak  # 升级到最新版
import pandas as pd

# 利用 AKShare 获取股票的后复权数据，这里只获取前 6 列
df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20240528', adjust="qfq")
df = df[['日期','股票代码','开盘','收盘','最高','最低','成交量','换手率']]
df.columns = ['trade_date', 'code','open', 'close', 'high', 'low','volume','turnover',]
df.trade_date = pd.to_datetime(df.trade_date)
df.to_csv('000007.csv')