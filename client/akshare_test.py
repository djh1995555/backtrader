from datetime import datetime
import akshare as ak  # 升级到最新版
import pandas as pd
import matplotlib.pyplot as plt
from factor_analyzer.factor_plotter import FactorPlotter

def get_stock_data():
    period="daily"
    start_date="20220301"
    end_date='20240528'
    adjust='qfq'

    stock_code = '000001'
    # # 利用 AKShare 获取股票的后复权数据，这里只获取前 6 列
    df = ak.stock_zh_a_hist(symbol=stock_code, period=period, start_date=start_date, end_date=end_date, adjust=adjust)
    df = df.drop(['股票代码','成交额','振幅','涨跌幅','涨跌额'], axis=1)
    df.日期 = pd.to_datetime(df.日期)
    df.to_csv(f'{stock_code}.csv')

    # 利用 AKShare 获取股票的后复权数据，这里只获取前 6 列
    etf_code = '159869'
    df = ak.fund_etf_hist_em(symbol=etf_code, period=period, start_date=start_date, end_date=end_date, adjust=adjust)
    df = df.drop(['成交额','振幅','涨跌幅','涨跌额'], axis=1)
    df.日期 = pd.to_datetime(df.日期)
    df.to_csv(f'{etf_code}.csv')

def get_total_volume():
    stock_sse_deal_daily_df = ak.stock_sse_deal_daily(date="20201111")
    print(stock_sse_deal_daily_df)

def get_runtime_stock_data():
    stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
    stock_zh_a_spot_em_df.to_csv('result.csv')

def get_stock_minute_data():
    stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol='sh600751', period='1', adjust="qfq")
    stock_zh_a_minute_df.to_csv('result.csv')
    stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol="000001", start_date="2024-03-20 09:30:00", end_date="2024-03-20 15:00:00", period="5", adjust="hfq")
    stock_zh_a_hist_min_em_df.to_csv('result2.csv')

def get_financial_data():
    stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(symbol="600004", start_year="2020")
    stock_financial_analysis_indicator_df.to_csv('financial_data.csv')

# stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(symbol="600004", start_year="2014")
# print(ak.stock_financial_analysis_indicator.__name__)
# stock_financial_analysis_indicator_df.to_csv(f'{ak.stock_financial_analysis_indicator.__name__}.csv')
# factor_plotter = FactorPlotter()
# # factor_plotter.plot(stock_financial_analysis_indicator_df, 20, "stock_financial_analysis_indicator")
# factor_plotter.plot_subfile(stock_financial_analysis_indicator_df,1, 21, ak.stock_financial_analysis_indicator.__name__,0)

def get_data(data_interface, **kwargs):
    df = data_interface(kwargs)
    factor_plotter = FactorPlotter()
    factor_plotter.plot(df, 20, data_interface.__name__)

# get_data(ak.stock_zh_a_hist,symbol="000003", start_date="20200101", end_date="20240101")

df = ak.stock_zh_a_hist(symbol="000003", start_date="20200101", end_date="20240101")
df.to_csv("result.csv")