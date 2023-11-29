import pandas as pd
df=pd.read_csv('station.csv',index_col='name')
print(df.loc['','code'])