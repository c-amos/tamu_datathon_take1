# initial imports ------------------------------------------------------------------
import pandas as pd
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# section title -----------------------------------------------------------------------------
url = 'https://fragilestatesindex.org/wp-content/uploads/2020/05/fsi-2020.xlsx'
urllib.request.urlopen(url, headers={'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
# ^ should retrieve excel file directly; double check

df = pd.read_excel(url)
#show first five rows of the data
df.head()
#to get the number of missing values
df.isnull().sum()
df.values.unique()
