# imports --------------------------------------------------------------------
import pandas as pd

# actual work and effort ---------------------------------------------------------
df = pd.read_csv('HFI.csv').drop(columns=['ISO_code','region']).sort_values('ef_rank')

df = df[['year','countries','hf_score','hf_rank']]
df = df.loc[df['hf_rank'] != '-']

df.to_csv('HFI.csv')
