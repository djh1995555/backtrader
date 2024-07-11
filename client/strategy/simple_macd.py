import backtrader as bt
from strategy.base_strategy import BaseStrategy
from backtrader.indicators import EMA

class SimpleMacd(BaseStrategy): 
    params = (
        ('maperiod', 15),
    )
    def __init__(self):
        super().__init__()
        me1 = EMA(self.data, period=12)
        me2 = EMA(self.data, period=26)
        self.diff = me1 - me2
        self.dea = EMA(self.diff, period=9)

        bt.indicators.MACDHisto(self.data)

    def next(self):
        # print(f"next data len:{len(self.data)} len:{len(self.diff)}")
        if self.order:
            return

        if not self.position:
            condition1 = self.diff[-1] - self.dea[-1]
            condition2 = self.diff[0] - self.dea[0]
            if condition1 < 0 and condition2 > 0:
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.order = self.buy()

        else:
            condition = (self.dataclose[0] - self.bar_executed_close) / self.dataclose[0]
            if condition > 0.1 or condition < -0.1:
                self.log('SELL CREATE, %.2f' % self.dataclose[0])
                self.order = self.sell()