# working with movehub csv

# imports ---------------------------------------------------------------------------
import pandas as pd
import numpy as np
#import seaborn as sn # remind me to un-comment this line whenever we start needing the visualizations

# read csv
df = pd.read_csv('movehubqualityoflife.csv').sort_values('Movehub Rating', ascending=False)
#print(df.head())

wow = np.arange(len(df))+1
#print(wow)
df.insert(2, 'Rank', wow)
print(df.set_index('Rank'))
