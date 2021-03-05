import csv
import plotly.figure_factory as ff
import pandas as spb

data = spb.read_csv("dataforhandw.csv")

fig = ff.create_distplot([data["Weight(Pounds)"].tolist()], ["weight"], show_hist=False)
fig.show()