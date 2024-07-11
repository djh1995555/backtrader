import backtrader as bt

class CustomBuySell(bt.observers.BuySell):
    params = (('barplot', True), ('bardist', 0.08))
    plotlines = dict(
        buy=dict(marker='^', markersize=8.0, color='c', fillstyle='full', ls=''),
        sell=dict(marker='v', markersize=8.0, color='pink', fillstyle='full', ls='')
    )