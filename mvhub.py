# working with movehub csv

# imports
import pandas as pd
import numpy as np
#import seaborn as sn

# read csv
df = pd.read_csv('movehubqualityoflife.csv').set_index('City')
print(df.head())


