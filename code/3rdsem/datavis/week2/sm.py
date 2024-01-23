import plotly.graph_objs as go
import numpy as np
from plotly.offline import plot
x=np.random.randn(2000)
y=np.random.randn(2000)
plot([go.Histogram2dContour(x=x, y=y),go.Scatter(x=x, y=y, mode='markers', marker=dict(color='white', size=3, opacity=0.3))],
       show_link=True)