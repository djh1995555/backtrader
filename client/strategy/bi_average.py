import backtrader as bt
from strategy.base_strategy import BaseStrategy
from backtrader.indicators import EMA

class BiAverage(BaseStrategy): 
    params = (
        ('maperiod', 15),
    )
    def __init__(self):
        super().__init__()
        me1 = EMA(self.data, period=12)
        me2 = EMA(self.data, period=26)
        self.diff = me1 - me2
        self.dea = EMA(self.diff, period=9)


    def next(self):
        print("======================")
        print('当前可用资金', self.broker.getcash())
        print('当前总资产', self.broker.getvalue())
        print('当前持仓量', self.getposition(self.data).size)
        print('当前持仓成本', self.getposition(self.data).price)
        print(f"dea:{self.dea[-1]}")
        # for x in self.dea:
        #     print(x)
        
        if(self.dea[-1] > 0.02 and self.broker.getcash() > 0):
            self.log('BUY CREATE, %.2f' % self.dataclose[0])
            self.order = self.buy()
        elif(self.dea[-1] < -0.01 and self.getposition(self.data).size > 0):
            self.log('SELL CREATE, %.2f' % self.dataclose[0])
            self.order = self.sell()