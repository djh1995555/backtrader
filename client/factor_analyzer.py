import akshare as ak
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from factor_analyzer.factor_plotter import FactorPlotter

class FactorAnalyzer():
    def __init__(self):
        pass

    def filter_extreme_n_sigma(self, series, n=3):
        mean = series.mean()
        std = series.std()
        max_range = mean + n*std
        min_range = mean - n*std
        return np.clip(series, min_range, max_range) 
      
    def standardize(self, series):
        mean = series.mean()
        std = series.std()
        return (series - mean)/std
    
    def neutral(factor,market_cap):
        y = factor
        x = market_cap
        result = sm.OLS(y.astype(float),x.astype(float)).fit()
        return result.resid

    def pre_process(self, df):
        # for i in range(1, len(df.columns)+1):
        #     df.iloc[:,i] = self.filter_extreme_percent(df.iloc[:,i])
        
        i = 2
        percentile = self.filter_extreme_n_sigma(df.iloc[:,i])
        percentile.plot()
        df.iloc[:,i].plot()
        plt.title(df.columns[i])
        plt.show()


def get_data(data_interface, **kwargs):
    df = data_interface(symbol=kwargs['symbol'], start_year=kwargs['start_year'])
    df.to_csv(f'{data_interface.__name__}.csv')
    factor_plotter = FactorPlotter()
    factor_plotter.plot(df, 20, data_interface.__name__)
    return df

period="daily"
start_date="20220301"
end_date='20240528'
adjust='qfq'
stock_code = '000001'

df = get_data(ak.stock_zh_a_hist, symbol=stock_code, period=period, start_date=start_date, end_date=end_date, adjust=adjust)
factor_analyzer = FactorAnalyzer()
factor_analyzer.pre_process(df)