from backtrader.plot.scheme import *

class PlotlyPlotScheme(PlotScheme):
    def __init__(self):
        super().__init__()
        self.rowsmajor = 1
        self.style = 'candle'
        self.barup = 'green'
        # decimal places of price for y-axis and hover of plot
        self.decimal_places = 5

        # maximum width of legend text
        self.max_legend_text_width = 16
