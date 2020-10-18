# imports --------------------------------------------------------------------
import pandas as pd

# actual work and effort ---------------------------------------------------------
df = pd.read_csv('HFI.csv').sort_values('hf_score',ascending=False)

df = df.loc[df['year'] == 2017]
df = df[['year','countries','hf_score','hf_rank']]
df = df.loc[df['hf_rank'] != '-']
df.set_index('hf_rank')

#print(df)

df.to_csv('HFI.csv')
