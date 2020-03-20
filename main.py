import json
import pandas as pd

import numpy as np

import matplotlib as matplotlib
import matplotlib.dates as mdates
matplotlib.use('agg')

import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict
from itertools import groupby

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()

result = open("data.json","r")

pythonObject = json.loads(result.read())

df = pd.DataFrame(pythonObject)

df_weeks = df.weeks
# print(df_weeks)

df_result = pd.DataFrame(columns=['w', 'a', 'd', 'c'])

for weeks in df_weeks:
    df_result = df_result.append(pd.DataFrame(weeks))

# print(df_result)

result = df_result.groupby(['w']).sum()
result = result.reset_index()


result = result.drop(result[result.c == 0].index)

result['date'] = pd.to_datetime(result['w'].astype(int), unit='s')

result.sort_values(by=['date'], inplace=True)

result['size'] = result['a'] - result['d']
result['size'] = result['size'].cumsum()

fig, ax = plt.subplots(figsize=(20, 10))

ax.plot('date', 'size', data=result)
plt.xlabel(u"Даты", fontsize=18)
plt.ylabel(u"Тысяч строк кода (KLOC)", fontsize=18)

plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)

plt.grid()


plt.savefig('base.png')

# df_new = df('weeks').apply(pd.Series).unstack().reset_indes().dropna()
#
#
# df.groupby(['weeks']).sum()


#
# for dict in dictArray:
#     print(dict['total'])