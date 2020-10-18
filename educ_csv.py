#imports --------------------------------------------------------------
import pandas as pd

# movehub -------------------------------------------------------------------------
df1 = pd.read_csv('movehubqualityoflife.csv')
ahhh = []
for i in range(0,len(df1)): ahhh.append(df1.iloc[i].City)
print(ahhh)

# fsi-2020 --------------------------------------------------------------------------
df = pd.read_excel('fsi-2020.xlsx').drop(columns=['Rank', 'Total',
       'C2: Factionalized Elites',
       'E3: Human Flight and Brain Drain',
       'S1: Demographic Pressures', 'S2: Refugees and IDPs',
       'X1: External Intervention', 'Change from Previous Year'],)

#print(df.columns)
