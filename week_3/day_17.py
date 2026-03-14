# Plotly consists of two key modules:

# plotly.graph_objects: Low-level API of Plotly that contains objects such as Figure, layout and data which are responsible for plotting.
# plotly.express: This is a high-level interface that simplifies the process of creating complex visualizations and and automatic styling.

import plotly.express as px

fig = px.line(x=[1, 2], y=[3, 4])

print(fig)

# customizations:
# Adjusting chart layout
# Adding annotations
# Customizing markers and lines

# line chart : syntax = plotly.express.line(data_frame=None, x=None, y=None, color=None, title=None)

import plotly.express as px

df = px.data.iris()

# fig = px.line(df, y="sepal_width",)
fig = px.line(df, y="sepal_width", line_dash='species',color='species')

fig.show()

#  bar chart : suntax = plotly.express.bar(data_frame=None, x=None, y=None, color=None, title=None)
import plotly.express as px

df = px.data.tips()

# fig = px.bar(df, x='day', y="total_bill")
fig = px.bar(df, x='day', y="total_bill", color='sex',facet_row='time',facet_col='sex')
# color: Used to color the bars.
# facet_row: Divides the graph into rows according to the data passed
# facet_col: Divides the graph into columns according to the data passed
fig.show()

# scatter plot = syntax = plotly.express.scatter(data_frame=None, x=None, y=None, color=None, title=None)

import plotly.express as px

df = px.data.tips()

# fig = px.scatter(df, x='total_bill', y="tip")
fig = px.scatter(df, x='total_bill', y="tip", color='time',symbol='sex', size='size', facet_row='day',facet_col='time')
# color: Color the points.
# symbol: Gives a symbol to each point according to the data passed.
# size: Size for each point.
fig.show()


# histogram = syntax = plotly.express.histogram(data_frame=None, x=None, y=None, color=None, nbins=None, histnorm=None, title=None, width=None, height=None)
import plotly.express as px

df = px.data.tips()

fig = px.histogram(df, x="total_bill")
# color: To color the bars
# nbins: To set the number of bins
# histnorm: Mode through which the bins are represented. Different values that can be passed using this argument.
# Here barmode can be either 'group', 'overlay' or 'relative'.

# group: Bars are stacked above zero for positive values and below zero for negative values
# overlay: Bars are drawn on the top of each other
# group: Bars are placed beside each other.
fig = px.histogram(df, x="total_bill", color='sex',nbins=50, histnorm='percent',barmode='overlay')
fig.show()

#  pie chart = syntax = plotly.express.pie(data_frame=None, names=None, values=None, color=None, hole=None, title=None, width=None, height=None)
# names: Column name for the pie chart labels.
# values: Column name for the size of the slices.
# hole: Creates a donut chart when set between 0 and 1.
# color_discrete_sequence: Strings defining valid CSS colors
# opacity: It finds how transparent or solid the markers (such as points on a scatter plot) appear. The value should be between 0 and 1
import plotly.express as px

df = px.data.tips()

fig = px.pie(df, values="total_bill", names="day")
fig = px.pie(df, values="total_bill", names="day",color_discrete_sequence=px.colors.sequential.RdBu,opacity=0.7, hole=0.5)
fig.show()

#  box plot = syntax = plotly.express.box(data_frame=None, x=None, y=None, color=None, facet_row=None, facet_col=None, title=None, width=None, height=None)
import plotly.express as px

df = px.data.tips()

fig = px.box(df, x="day", y="tip")
fig = px.box(df, x="day", y="tip", color='sex',facet_row='time', boxmode='group',notched=True)
fig.show()
# color: used to assign color to marks
# facet_row: assign marks to facetted subplots in the vertical direction
# facet_col: assign marks to facetted subplots in the horizontal direction
# boxmode: One of ‘group’ or ‘overlay’ In ‘overlay’ mode, boxes are on drawn top of one another. In ‘group’ mode, boxes are placed beside each other.
# notched: If True, boxes are drawn with notches

# violin plot = syntax = plotly.express.violin(data_frame=None, x=None, y=None, color=None, facet_row=None, facet_col=None, title=None, width=None, height=None)
import plotly.express as px

df = px.data.tips()

fig = px.violin(df, x="day", y="tip")
fig = px.violin(df, x="day", y="tip", color='sex',facet_row='time', box=True)
fig.show()

# 3D scatter plot = syntax = plotly.express.scatter_3d(data_frame=None, x=None, y=None, z=None, color=None, symbol=None, size=None, title=None, width=None, height=None)

import plotly.express as px

df = px.data.tips()

fig = px.scatter_3d(df, x="total_bill", y="sex", z="tip")
fig = px.scatter_3d(df, x="total_bill", y="sex", z="tip", color='day', size='total_bill', symbol='time')
fig.show()


# Implementing Interactive Features in Plotly
# 1. Dropdown Menu = A drop-down menu allows users to select different options to modify the chart. The update method is used to control the chart based on dropdown choices. In plotly there are 4 possible methods to modify the charts by using update menu method.

# restyle: modify data or data attributes
# relayout: modify layout attributes
# update: modify data and layout attributes
# animate: start or pause an animation

import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

df = px.data.tips()

plot = go.Figure(data=[go.Scatter(
    x=df['day'],
    y=df['tip'],
    mode='markers',)
])

plot.update_layout(
    updatemenus=[
        dict(buttons=list([
            dict(
                args=["type", "scatter"],
                label="Scatter Plot",
                method="restyle"
            ),
            dict(
                args=["type", "bar"],
                label="Bar Chart",
                method="restyle"
            )
        ]),
            direction="down",
        ),
    ]
)

plot.show()

# 2. Adding Buttons = In plotly, adding custom Buttons are used to quickly make actions directly from a record. Custom Buttons can be added to page layouts in CRM, Marketing and Custom Apps. There are also 4 possible methods that can be applied in custom buttons:
# restyle: modify data or data attributes
# relayout: modify layout attributes
# update: modify data and layout attributes
# animate: start or pause an animation
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

df = px.data.tips()

plot = go.Figure(data=[go.Scatter(
    x=df['day'],
    y=df['tip'],
    mode='markers',)
])

plot.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="left",
            buttons=list([
                dict(
                    args=["type", "scatter"],
                    label="Scatter Plot",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Bar Chart",
                    method="restyle"
                )
            ]),
        ),
    ]
)

plot.show()

# 3. Creating Sliders and Selectors to the Plot - In Plotly, the range slider is an input control that allows users to select a value range between a specified minimum and maximum. It allows selecting pre-configured ranges and manually inputting minimum and maximum values or dates.
import plotly.graph_objects as px
import plotly.express as go
import numpy as np

df = go.data.tips()

x = df['total_bill']
y = df['tip']

plot = px.Figure(data=[px.Scatter(
    x=x,
    y=y,
    mode='markers',)
])

plot.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                    step="day",
                    stepmode="backward"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
    )
)

plot.show()


# Building Interactive Dashboards with Plotly Dash
# import dash
# from dash import dcc, html
# import plotly.express as px
# import pandas as pd

# df = pd.DataFrame({
#     'x': [1, 2, 3, 4, 5],
#     'y': [10, 15, 13, 17, 14]
# })

# app = dash.Dash(__name__)

# app.layout = html.Div([
#     dcc.Graph(
#         id='example-graph',
#         figure=px.scatter(df, x='x', y='y', title='Scatter Plot in Dash')
#     )
# ])

# if __name__ == '__main__':
#     app.run(debug=True, port=8050)