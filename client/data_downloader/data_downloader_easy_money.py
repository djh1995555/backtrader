import backtrader as bt
import akshare as ak
import pandas as pd
from data_downloader.data_downloader import DataDownloader

# 东方财富
class PandasDataEastMoney(bt.feeds.PandasData):
    lines = ('turnover',)
    params = (
    ('datetime', 0),
    ('open', 2),
    ('close', 3),
    ('high', 4),
    ('low', 5),
    ('volume', 6),
    ('turnover', 7),)

class DataDownloaderEastMoney(DataDownloader):
    def download(self, stock_list, start_date, end_date, period, adjust):
        for stock_code in stock_list:
            df = ak.stock_zh_a_hist(symbol=stock_code, period=period, start_date=start_date, end_date=end_date, adjust=adjust)
            df.日期 = pd.to_datetime(df.日期)
            self.stock_data_dict_[stock_code] = PandasDataEastMoney(dataname=df)
        return self.stock_data_dict_
    
