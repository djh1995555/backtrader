import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# 创建一个示例DataFrame
data = {'时间': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
        '项1': [10, 20, 15, 25],
        '项2': [5, 15, 10, 20],
        '项3': [8, 18, 12, 22]}
df = pd.DataFrame(data)

# 创建子图
fig = make_subplots(rows=len(df.columns)-1, cols=1, subplot_titles=df.columns[1:])

# 绘制每列数据的子图
for i, col in enumerate(df.columns[1:]):
    fig.add_trace(go.Scatter(x=df['时间'], y=df[col], mode='lines', name=col), row=i+1, col=1)

# 设置布局
fig.update_layout(title='每列数据的子图', title_x=0.45, title_font=dict(size=30, family="Arial", weight="bold"), showlegend=True)

# 显示图表
fig.show()