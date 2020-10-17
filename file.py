print('Hello World!')
# something else

url = 'https://fragilestatesindex.org/wp-content/uploads/2020/05/fsi-2020.xlsx'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(url)
#show first five rows of the data
df.head()
#to get the number of missing values
df.isnull().sum()
df.values.unique()
