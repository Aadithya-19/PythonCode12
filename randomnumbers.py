import random
import plotly.figure_factory as ff
import plotly.express as ps
import pandas as spb

dice_result = []
count = []

for i in range(0, 100):
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    dice_result.append(num1+num2)
    count.append(i)

fig = ff.create_distplot([dice_result], ["result"])
fig.show()