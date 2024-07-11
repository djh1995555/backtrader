import backtrader as bt
import akshare as ak
import pandas as pd
from data_downloader.data_downloader import DataDownloader

# 东方财富
class PandasDataEastMoney(bt.feeds.PandasData):
    lines = ('turnover',)
    params = (
    ('datetime', 0),
    ('open', 1),
    ('close', 2),
    ('high', 3),
    ('low', 4),
    ('volume', 5),
    ('turnover', 6),)

class DataDownloaderEastMoney(DataDownloader):
    def download_stock(self, stock_list, start_date, end_date, period, adjust):
        for stock_code in stock_list:
            df = ak.stock_zh_a_hist(symbol=stock_code, period=period, start_date=start_date, end_date=end_date, adjust=adjust)
            df = df.drop(['股票代码'], axis=1)
            df.日期 = pd.to_datetime(df.日期)
            self.stock_data_dict_[stock_code] = PandasDataEastMoney(dataname=df)
        return self.stock_data_dict_
    
    def download_etf(self, etf_list, start_date, end_date, period, adjust):
        for etf_code in etf_list:
            df = ak.fund_etf_hist_em(symbol=etf_code, period=period, start_date=start_date, end_date=end_date, adjust=adjust)
            df = df.drop(['成交额','振幅','涨跌幅','涨跌额'], axis=1)
            df.日期 = pd.to_datetime(df.日期)
            self.stock_data_dict_[etf_code] = PandasDataEastMoney(dataname=df)
        return self.stock_data_dict_    
