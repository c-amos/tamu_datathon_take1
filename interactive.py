# imports ---------------------------------------------------------------------
import pandas as pd

# 'overall_df' is going to come from a data file we make when we get all of the columns we want to use
# write bigger dataframe
df = pd.read_csv('movehubqualityoflife.csv').drop(columns=['Rank','Rank.1'])
#print(df.columns)

df2 = pd.read_csv('HFI.csv'
  ).drop(columns=[
       'year', # only using 2017
       'Unnamed: 0'] # using dataframes to create other dataframes creates this 'Unnamed' column for the frame's orig index, then adds its own new index
  ).rename(columns={'countries':'Country'}) # column name consistency

#print(df2)

# match countries between df and df2 ----------------------------------------------------------------

## create columns from df2
for name in (df2.columns):
  if name in df.columns: pass
  else: df[name] = 0.0

for i in range(0,len(df)):
  #print(df.iloc[i].hf_score)
  value = df2.loc[df2.Country == df.iloc[i].Country]
  #print(value)
  #print(float(value.hf_score))
  try: df.loc[i,'hf_score'] = float(value.hf_score)
  except: pass
  try: df.loc[i,'hf_rank'] = int(value.hf_rank)
  except: pass
  print('\r'+str(i)+' out of '+str(len(df))+' complete',end='')

#print(df)

df.to_csv('homestretch.csv')

# ask for user input ----------------------------------------------------------
overall_df = pd.read_csv('homestretch.csv').drop(columns=['Unnamed: 0','lat','lng','City','hf_rank','Country'])
#print(overall_df.columns)

using = list(overall_df.columns)
print(using)

for index in using:
  inp = input(f'How much do you value {index} on a scale from 1 to 10?\t')
  overall_df[index] = int(inp)*overall_df[index]

print(overall_df)

# end total score column ----------------------------------------------------------------------------
overall_df['End Total Score'] =

# sum the values in each index (i.e. column) for each city (i.e. row), then rank the cities by total value; return a ranked list
# e.g. Ulaanbaatar totals at 400, Sao Paulo at 300, Gaborone at 200; therefore, 1,2,3
