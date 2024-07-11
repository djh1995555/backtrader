import os
import mpld3
import backtrader as bt
import pandas as pd
from strategy.simple_macd import SimpleMacd
from strategy.simple_kdj import SimpleKDJ
from strategy.bi_average import BiAverage
from data_downloader.data_downloader_easy_money import DataDownloaderEastMoney
from observer.order_observer import OrderObserver
from observer.custom_buy_sell import CustomBuySell
from plotter.plotly_plotter import PlotlyPlotter
from plotter.plotly_scheme import PlotlyPlotScheme
import plotly.io

cerebro = bt.Cerebro(stdstats=False) # False表示默认的Broker，Trades，BuySell不会出现在可视化结果中，需要主动指定
# cerebro = bt.Cerebro()

stock_codes = [
    '000001',
    # '000002',
]
etf_codes = [
    '159869',
]
start_date='20170301'
end_date='20240528'
period = 'daily'
adjust = 'qfq'
data_downloader = DataDownloaderEastMoney()
# data_dict = data_downloader.download_stock(stock_codes, start_date, end_date, period, adjust)
data_dict = data_downloader.download_etf(etf_codes, start_date, end_date, period, adjust)
for stock_code, data in data_dict.items():
    cerebro.adddata(data, name=stock_code)
    cerebro.addobserver(bt.observers.Benchmark, data=data)
    cerebro.addobserver(CustomBuySell)

    cerebro.addobserver(bt.observers.Broker)
    cerebro.addobserver(bt.observers.Trades)
    # cerebro.addobserver(bt.observers.BuySell)

    cerebro.addobserver(bt.observers.DrawDown)
    cerebro.addobserver(bt.observers.TimeReturn)
    # cerebro.addobserver(OrderObserver) # custom observer

    cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name='_AnnualReturn')  # 年化收益率
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='_SharpeRatio')  # 夏普比率
    cerebro.addanalyzer(bt.analyzers.SharpeRatio_A, _name='_SharpeRatio_A')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='_DrawDown')  # 回撤
    cerebro.addanalyzer(bt.analyzers.Returns, _name='_Returns', tann=252)
    cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='_TimeReturn')

cerebro.addstrategy(BiAverage)

cerebro.broker.setcash(10000)
cerebro.addsizer(bt.sizers.FixedSize, stake=100)
cerebro.broker.setcommission(commission=0.005)

result = cerebro.run()
strat = result[0]
# print("--------------- _TimeReturn -----------------")
# print(strat.analyzers._TimeReturn.get_analysis())
# print("--------------- AnnualReturn -----------------")
# print(strat.analyzers._AnnualReturn.get_analysis())
# print("--------------- SharpeRatio -----------------")
# print(strat.analyzers._SharpeRatio.get_analysis())
# print("--------------- DrawDown -----------------")
# print(strat.analyzers._DrawDown.get_analysis())

# analyzer = {}
# analyzer['年化收益率'] = result[0].analyzers._Returns.get_analysis()['rnorm']
# analyzer['年化收益率（%）'] = result[0].analyzers._Returns.get_analysis()['rnorm100']
# # 提取最大回撤
# analyzer['最大回撤（%）'] = result[0].analyzers._DrawDown.get_analysis()['max']['drawdown'] * (-1)
# # 提取夏普比率
# analyzer['年化夏普比率'] = result[0].analyzers._SharpeRatio_A.get_analysis()['sharperatio']


# cerebro.plot()
scheme = PlotlyPlotScheme()
figs = cerebro.plot(PlotlyPlotter(show=False, scheme=scheme))

# directly manipulate object using methods provided by `plotly`
for i, each_run in enumerate(figs):
    for j, each_strategy_fig in enumerate(each_run):

        # save the html of the plot to a variable
        html = plotly.io.to_html(each_strategy_fig, full_html=False)

        # 创建完整的 HTML 内容
        full_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Quant Backtest Result</title>
        </head>
        <body>
            <div style="text-align: center;">
                <h1>Quant Backtest Result</h1>
                <p style="font-family: Arial, sans-serif; font-size: 16px; font-weight: bold;">
                    年化收益率(%): {result[0].analyzers._Returns.get_analysis()['rnorm100']:.3f}    ,
                    最大回撤(%): {result[0].analyzers._DrawDown.get_analysis()['max']['drawdown'] * (-1):.3f}    ,
                    年化夏普比率: {result[0].analyzers._SharpeRatio_A.get_analysis()['sharperatio']:.3f}
                </p>
            </div>
            {html}
        </body>
        </html>
        """

        # 写入 HTML 文件
        output_dir_name = 'output'
        if not os.path.exists(output_dir_name):
            os.makedirs(output_dir_name)
        output_file_name = os.path.join(output_dir_name, f'{i}_{j}.html')
        with open(output_file_name, 'w') as f:
            f.write(full_html)
