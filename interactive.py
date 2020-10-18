# imports ---------------------------------------------------------------------
import pandas as pd

# 'overall_df' is going to come from a data file we make when we get all of the columns we want to use

# ask for user input ----------------------------------------------------------
for index in overall_df.columns:
  inp = input(f'How much do you value {index} on a scale from 1 to 10?')
  overall_df[index] = int(inp)*overall_df[index]

# sum the values in each index (i.e. column) for each city (i.e. row), then rank the cities by total value; return a ranked list
# e.g. Ulaanbaatar totals at 400, Sao Paulo at 300, Gaborone at 200; therefore, 1,2,3
