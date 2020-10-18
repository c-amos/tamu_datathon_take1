# imports --------------------------------------------------------------------
import pandas as pd

# actual work and effort ---------------------------------------------------------
df = pd.read_csv('HFI.csv').drop(columns=['ISO_code','region']).sort_values('ef_rank')

for i in range(0,len(df)):
  if (df.iloc[i]['ef_rank'].isnumeric()): df['Drop?'] = False
  else: df['Drop?'] = True
  print('\r'+str(i) + ' out of ' + str(len(df)) + ' complete',end='')

for i in range(0,len(df)):
  if (df.iloc[i]['Drop?'] == True: df.drop
  else: df['Drop?'] = True
  print('\r'+str(i) + ' out of ' + str(len(df)) + ' complete',end='')

print('\n',df)
