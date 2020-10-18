# working with movehub csv

# imports ---------------------------------------------------------------------------
import pandas as pd
import numpy as np
#import seaborn as sn # remind me to un-comment this line whenever we start needing the visualizations

# read csv
df = pd.read_csv('movehubqualityoflife.csv')
#print(df.head())

# reversing crime ratings for accuracy
df['Safety Rating'] = 100 - df['Crime Rating']
df['1 - Pollution'] = 100 - df['Pollution']
df = df.drop(columns=['Crime Rating','Pollution'])

# calculating end totals
temp_df = df[['Safety Rating','Purchase Power','Health Care','Pollution','Quality of Life']]

vars = []
for row in range(0,len(df)):
  var = 0
  for col in temp_df:
    obj = temp_df[col].iloc[row]
    var += obj
  vars.append(var)

# adding end totals of scores
df.insert(len(df.columns),'Totals',vars)
print(df)

# turn totals into rankings
df = df.sort_values(by='Totals')

# weighting system
df['Pollution'] = 4*df['Pollution']

ax = sn.barplot(x=['City'],y=['Totals']) # fix this
plt.show()
