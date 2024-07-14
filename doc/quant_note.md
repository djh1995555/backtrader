# Backtrader
# Alphalens图表分析


# [经典策略](https://www.myquant.cn/docs/python_strategyies/103)
# [因子](https://blog.csdn.net/m0_67510277/article/details/137567493)

## 行情因子
- 50ETF 期权波动率指数：```df = ak.index_option_50etf_qvix()```
- 股票整体行情：```df = ak.stock_sse_deal_daily(date="20201111")```
- 股票实时行情：```df = ak.stock_zh_a_spot_em()```
- 股票历史行情：```df = ak.stock_zh_a_hist(stock_code, period, start_date, end_date, adjust)```
- 股票历史分时行情（新浪）：```df = ak.stock_zh_a_minute(symbol='sh600751', period='1', adjust="qfq")```
- 股票历史分时行情（东财）：```df = ak.stock_zh_a_hist_min_em(stock_code, start_date, end_date=, period, adjust)```
- ETF历史行情：```df = ak.fund_etf_hist_em(etf_code, period, start_date, end_date, adjust )```
- 沪市融资融券：```df = ak.stock_margin_detail_sse(date="20230922")```
- 深市融资融券：```df = ak.stock_margin_detail_szse(date="20230925")```
- 
## 财务因子
### 详细
归母净利润，营业总收入，营业成本，净利润，扣非净利润，股东权益合计(净资产)，商誉，经营现金流量净额，基本每股收益，每股净资产，每股现金流，净资产收益率(ROE)，总资产报酬率(ROA)，毛利率，销售净利率，期间费用率，资产负债率，基本每股收益，稀释每股收益，摊薄每股净资产_期末股数，调整每股净资产_期末股数，每股净资产_最新股数，每股经营现金流，每股现金流量净额，每股企业自由现金流量，每股股东自由现金流量，每股未分配利润，每股资本公积金，每股盈余公积金，每股留存收益，每股营业收入，每股营业总收入，每股息税前利润，净资产收益率(ROE)，摊薄净资产收益率，净资产收益率_平均，净资产收益率_平均_扣除非经常损益，摊薄净资产收益率_扣除非经常损益，息税前利润率，总资产报酬率，总资本回报率，投入资本回报率，息前税后总资产报酬率_平均，毛利率，销售净利率，成本费用利润率，营业利润率，总资产净利率_平均，总资产净利率_平均(含少数股东损益)，归母净利润，营业总收入，净利润，扣非净利润，营业总收入增长率，归属母公司净利润增长率，经营活动净现金/销售收入，经营性现金净流量/营业总收入，成本费用率，期间费用率，销售成本率，经营活动净现金/归属母公司的净利润，所得税/利润总额，流动比率，速动比率，保守速动比率，资产负债率，权益乘数，权益乘数(含少数股权的净资产)，产权比率，现金比率，应收账款周转率，应收账款周转天数，存货周转率，存货周转天数，总资产周转率，总资产周转天数，流动资产周转率，流动资产周转天数，应付账款周转率
- 盈利能力：
- 杠杆水平：
- 流动性：
- 成长性：
- 经营能力：
### 接口
```df = ak.stock_financial_abstract(symbol="600004")```
```df = ak.stock_financial_analysis_indicator(symbol="600004", start_year="2020")```

## 估值因子
### 详细
市盈率，市盈率TTM，市净率，市销率，市销率TTM，股息率，股息率TTM，总市值
### 接口
```df = ak.stock_a_indicator_lg(symbol="000001")```

## 宏观因子
### 中国宏观
- 企业商品价格指数（农产品，矿产品，煤油电）：```macro_china_qyspjg_df = ak.macro_china_qyspjg()```
- 社会融资规模增量统计：```df = ak.macro_china_shrzgm()```
- 中国 GDP 年率：```df = ak.macro_china_gdp_yearly()```
- 国内生产总值：```df = ak.macro_china_gdp()```
- 中国 CPI 月率：```df = ak.macro_china_cpi_monthly()```
- 居民消费价格指数：```df = ak.macro_china_cpi()```
- 商品零售价格指数：```df = ak.macro_china_retail_price_index()```
- 中国 PPI 年率：```df = ak.macro_china_ppi_yearly()```
- 工业品出厂价格指数：```df = ak.macro_china_ppi()```
- 官方制造业 PMI：```df = ak.macro_china_pmi_yearly()```
- 采购经理人指数：```df = ak.macro_china_pmi()```
- 外汇储备：```df = ak.macro_china_fx_reserves_yearly()```
- 央行黄金和外汇储备：```df = ak.macro_china_foreign_exchange_gold()```
- 上海黄金交易所报告：```df = ak.macro_china_au_report()```
- M2货币供应年率：```df = ak.macro_china_m2_yearly()```
- 货币供应量：```df = ak.macro_china_supply_of_money()```
- 中国货币供应量：```df = ak.macro_china_money_supply()```
- 企业景气及企业家信心指数：```df = ak.macro_china_enterprise_boom_index()```
- 消费者信心指数：```df = ak.macro_china_xfzxx()```
- 全国税收收入：```df = ak.macro_china_national_tax_receipts()```
- 财政收入：```df = ak.macro_china_czsr()```
- 新增信贷数据：```df = ak.macro_china_new_financial_credit()```
- 海关进出口增减情况：```df = ak.macro_china_hgjck()```
- 存款准备金率：```df = ak.macro_china_reserve_requirement_ratio()```
- 社会消费品零售总额：```df = ak.macro_china_consumer_goods_retail()```
- 人民币兑美元汇率：```df = ak.currency_boc_sina(symbol="美元", start_date="20230304", end_date="20231110")```


### 美国宏观
- 美国GDP：```df = ak.macro_usa_gdp_monthly()```
- 美国CPI月率报告：```df = ak.macro_usa_cpi_monthly()```
- 美国核心CPI月率报告：```df = ak.macro_usa_core_cpi_monthly()```
- 美国生产者物价指数(PPI)报告：```df = ak.macro_usa_ppi()```
- 美国核心生产者物价指数(PPI)报告：```df = ak.macro_usa_core_ppi()```
- 美国零售销售月率报告：```df = ak.macro_usa_retail_sales()```
- 美国出口价格指数报告：```df = ak.macro_usa_export_price()```
- 美国进口物价指数报告：```df = ak.macro_usa_import_price()```
- 美联储劳动力市场状况指数报告：```df = ak.macro_usa_lmci()```
- 美国失业率报告：```df = ak.macro_usa_unemployment_rate()```
- 美国非农就业人数报告：```df = ak.macro_usa_non_farm()```

### 利率
- 美联储利率决议报告：```df = ak.macro_bank_usa_interest_rate()```
- 欧洲央行决议报告：```df = ak.macro_bank_euro_interest_rate()```
- 英国央行决议报告：```df = ak.macro_bank_english_interest_rate()```
- 日本利率决议报告：```df = ak.macro_bank_japan_interest_rate()```
- 印度利率决议报告：```df = ak.macro_bank_india_interest_rate()```
- 银行间拆借利率：```df = ak.rate_interbank(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="3月")```
- 中美国债收益率：```df = ak.bond_zh_us_rate(start_date="19901219")```
- 
### 国际宏观
- 黄金：```df = ak.macro_cons_gold()```
- 白银：```df = ak.macro_cons_silver()```
- 石油：```df = ak.macro_cons_opec_month()```
- 能源指数：```df = ak.macro_china_energy_index()```
- 大宗商品价格：```df = ak.macro_china_commodity_price_index()```
- 费城半导体指数：```df = ak.macro_global_sox_index()```
- 义乌小商品指数-电子元器件：```df = ak.macro_china_yw_electronic_index()```
- 原油运输指数：```df = ak.macro_china_bdti_index()```
- 超灵便型船运价指数：```df = ak.macro_china_bsi_index()```
- 海岬型运费指数：```df = ak.macro_shipping_bci()```
- 巴拿马型运费指数：```df = ak.macro_shipping_bpi()```
- 成品油运输指数：```df = ak.macro_shipping_bcti()```
