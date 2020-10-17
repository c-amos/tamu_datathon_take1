# initial imports ------------------------------------------------------------------
import pandas as pd
import urllib.request
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns

# section title -----------------------------------------------------------------------------
url = 'https://fragilestatesindex.org/wp-content/uploads/2020/05/fsi-2020.xlsx'
urllib.request.Request(url, headers={'User-agent' : 'Mozilla/5.0'})
# ^ should retrieve excel file directly; double check

df = pd.read_excel(url)
#show first five rows of the data
df.head()
#to get the number of missing values
df.isnull().sum()
df.values.unique()
