# working with movehub csv

# imports
import pandas as pd
import numpy as np
#import seaborn as sn

# read csv
df = pd.read_csv('movehubqualityoflife.csv').set_index('City')
#print(df.head())

# reversing crime ratings for accuracy
df['Safety Rating'] = 100 - df['Crime Rating']
df = df.drop(columns='Crime Rating')

# calculating end totals
temp_df = df[['Safety Rating','Purchase Power','Health Care','Pollution','Quality of Life']]

vars = []
for row in range(0,len(df)):
  var = 0
  for col in temp_df:
    obj = temp_df[col].iloc[row]
    var += obj
  vars.append(var)

df.insert(len(df.columns),'Totals',vars)
print(df)

# adding end totals of scores
# print(len(df.iloc[1]))
