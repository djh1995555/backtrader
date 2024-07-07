import backtrader as bt

class CustomBuySell(bt.observers.BuySell):
    params = (('barplot', True), ('bardist', 0.02))
    plotlines = dict(
    buy=dict(marker=r'$\Uparrow$', markersize=10.0, color='#d62728' ),
    sell=dict(marker=r'$\Downarrow$', markersize=10.0, color='#2ca02c'))