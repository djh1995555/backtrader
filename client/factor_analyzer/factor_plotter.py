import os
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

class FactorPlotter():
    def __init__(self):
        pass

    def plot(self, df, subplots_num_per_file, output_filename):
        self.output_dir_ = os.path.join('output', 'factor', output_filename)
        if(not os.path.exists(self.output_dir_)):
            os.makedirs(self.output_dir_)
        output_csv = os.path.join(self.output_dir_, f"{output_filename}.csv")
        df.to_csv(output_csv)

        for i in range(int((df.shape[1] - 1) / subplots_num_per_file)):
            print(i)
            self.plot_subfile(df, i * subplots_num_per_file + 1, i * subplots_num_per_file + 1 + subplots_num_per_file, output_filename, i)
        i += 1
        self.plot_subfile(df, 
                          i * subplots_num_per_file + 1, 
                          min(i * subplots_num_per_file + 1 + subplots_num_per_file, df.shape[1] - 1), 
                          output_filename, 
                          i
                          )

    def plot_subfile(self, df, start_idx, end_idx, output_filename, file_idx):
        print(f"{start_idx},{end_idx}")
        subplots_num = end_idx - start_idx
        subplot_height = 200
        fig = make_subplots(rows=subplots_num, 
                            cols=1, 
                            shared_xaxes=True,
                            # vertical_spacing=0.05,
                            row_heights=[subplot_height]*subplots_num,
                            subplot_titles=df.columns[start_idx:end_idx+1]
                            )

        for i in range(start_idx, end_idx):
            fig.add_trace(go.Scatter(x=df['日期'], y=df.iloc[:,i], mode='lines', name=df.columns[i]), row=i-start_idx+1, col=1)

        fig.update_layout(
            title=f"{output_filename}_{file_idx}", 
            title_x=0.45, 
            title_font=dict(
                size=30, 
                family="Arial",
                weight="bold"
                ), 
            showlegend=True,
            height=subplots_num*subplot_height,
        )

        output_fullname = os.path.join(self.output_dir_, f"{output_filename}_{file_idx}.html")
        fig.write_html(output_fullname)