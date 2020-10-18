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

# introduction ------------------------------------------------------------------------------------
print("This script is designed to take user input regarding their opinions on factors involved in their ideal quality of life.",
"The script will use this information to aggregate a 'score' regarding the fitness of each city, listing the top and bottom five.")

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
  print('\r'+str(i+1)+' out of '+str(len(df))+' complete',end='')
print('Loading complete')

#print(df)

df.to_csv('homestretch.csv')

# ask for user input ----------------------------------------------------------
overall_df = pd.read_csv('homestretch.csv').drop(columns=['Unnamed: 0','lat','lng','hf_rank','Country'])
#print(overall_df.columns)

using = list(overall_df.columns)
using.remove('City')
#print(using)
print('\n')
for index in using:
  inp = input(f'How much do you value {index} on a scale from 1 to 10?\t')
  overall_df[index] = int(inp)*overall_df[index]

#print(overall_df)

overall_df['End Total'] = 0.0

# end total score column ----------------------------------------------------------------------------
for i in range(0,len(overall_df)):
  sum = 0.0
  for element in overall_df.iloc[i]:
    try: sum += element
    except: pass
  overall_df.loc[i,'End Total'] = sum

#overall_df['End Total Score'] =
# sum the values in each index (i.e. column) for each city (i.e. row), then rank the cities by total value; return a ranked list
# e.g. Ulaanbaatar totals at 400, Sao Paulo at 300, Gaborone at 200; therefore, 1,2,3

overall_df.to_csv('final_prod.csv')
working_df = pd.read_csv('final_prod.csv').sort_values('End Total',ascending=False).set_index('End Total')
#print(working_df)
print("Your top 5 suggested cities are: ")
print(working_df.City.head())
print("Your top 5 LEAST suggested cities are: ")
print(working_df.City.tail())
