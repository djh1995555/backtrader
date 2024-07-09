import mpld3
import backtrader as bt
import pandas as pd
from strategy.simple_macd import SimpleMacd
from strategy.simple_kdj import SimpleKDJ
from strategy.null import NULL
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
start_date='20170301'
end_date='20240528'
period = 'daily'
adjust = 'qfq'
data_downloader = DataDownloaderEastMoney()
data_dict = data_downloader.download(stock_codes, start_date, end_date, period, adjust)
for stock_code, data in data_dict.items():
    cerebro.adddata(data, name=stock_code)
    cerebro.addobserver(bt.observers.Benchmark, data=data)
    # cerebro.addobserver(CustomBuySell)

    cerebro.addobserver(bt.observers.Broker)
    # cerebro.addobserver(bt.observers.Trades)
    cerebro.addobserver(bt.observers.BuySell)

    cerebro.addobserver(bt.observers.DrawDown)
    cerebro.addobserver(bt.observers.TimeReturn)
    # cerebro.addobserver(OrderObserver) # custom observer

    # cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name='_AnnualReturn')  # 年化收益率
    # cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='_SharpeRatio')  # 夏普比率
    # cerebro.addanalyzer(bt.analyzers.SharpeRatio_A, _name='_SharpeRatio_A')
    # cerebro.addanalyzer(bt.analyzers.DrawDown, _name='_DrawDown')  # 回撤
    # cerebro.addanalyzer(bt.analyzers.Returns, _name='_Returns', tann=252)
    # cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='_TimeReturn')

cerebro.addstrategy(SimpleMacd)

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
# # 提取年化收益
# analyzer['年化收益率'] = result[0].analyzers._Returns.get_analysis()['rnorm']
# analyzer['年化收益率（%)'] = result[0].analyzers._Returns.get_analysis()['rnorm100']
# # 提取最大回撤
# analyzer['最大回撤（%)'] = result[0].analyzers._DrawDown.get_analysis()['max']['drawdown'] * (-1)
# # 提取夏普比率
# analyzer['年化夏普比率'] = result[0].analyzers._SharpeRatio_A.get_analysis()['sharperatio']


# cerebro.plot()
scheme = PlotlyPlotScheme()
figs = cerebro.plot(PlotlyPlotter(show=False, scheme=scheme))

# directly manipulate object using methods provided by `plotly`
for i, each_run in enumerate(figs):
    for j, each_strategy_fig in enumerate(each_run):
        # open plot in browser
        each_strategy_fig.show()

        # save the html of the plot to a variable
        # html = plotly.io.to_html(each_strategy_fig, full_html=False)

        # write html to disk
        plotly.io.write_html(each_strategy_fig, f'{i}_{j}.html', full_html=True)

# cerebro.plot()
