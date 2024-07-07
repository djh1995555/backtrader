import backtrader as bt
import csv

class BaseStrategy(bt.Strategy):
    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    @staticmethod
    def percent(today, yesterday):
        return float(today - yesterday) / today

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.volume = self.datas[0].volume

        self.order = None
        self.buyprice = None
        self.buycomm = None

        self.mystats = csv.writer(open("mystats.csv", "w"))
        self.mystats.writerow(['datetime',
                               'drawdown', 
                               'maxdrawdown',
                               'timereturn',
                               'value', 
                               'cash',
                               ])

    def write(self, date):
        self.mystats.writerow([date.strftime('%Y-%m-%d'),
                               '%.4f' % self.stats.drawdown.drawdown[0],
                               '%.4f' % self.stats.drawdown.maxdrawdown[0],
                               '%.4f' % self.stats.timereturn.line[0],
                               '%.4f' % self.stats.broker.value[0],
                               '%.4f' % self.stats.broker.cash[0]])
    def write_next(self):
        self.write(self.data.datetime.date(-1))

    def write_stop(self):
        self.write(self.data.datetime.date(0))