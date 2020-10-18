# working with movehub csv

# imports ---------------------------------------------------------------------------
import pandas as pd
import numpy as np
#import seaborn as sn # remind me to un-comment this line whenever we start needing the visualizations

# read csv ---------------------------------------------------------------------------------------
df = pd.read_csv('movehubqualityoflife.csv').sort_values('Movehub Rating', ascending=False)

# -------------------------------------------------------------------
wow = np.arange(len(df))
#print(len(wow))
df.insert(2, 'Rank', wow)

# doing the whole thing we just did --------------------------------------------------
df = df.set_index('Rank',drop=False)

other_csv = pd.read_csv('sample.csv')
#print(len(other_csv.Country))

df.insert(len(df.columns),'Country',other_csv.Country)
df['Rank'] = df['Rank'] + 1

#print(df)

le_df = pd.read_csv('LifeExpectancy.csv')
print(le_df)
