import pandas as pd
import missingno as msno

data = {'x':[1,2,3], 'y':['a', 'b', 'c'], 'z': [False, True, False]}
df = pd.DataFrame(data)
df[['x','y']]
df.loc[0]
df['new_column'] = -1
df.head()
df[df['z']]
df['x'] == 2
df.shape
pd.concat([df, df], axis=0, sort=False)
pd.concat([df, df], axis=1)
df.merge(df.head(2), on='y', how='left')

# Analyze dataset for cleaning
data = pd.read_csv('Data_Science_Apps/data/Eastern Front.csv')
data.head()
data.tail()
data.sample(n=5)
data.dtypes
list(data.columns)

battles = data[data.level == 100]
battles.shape
columns = ['Location', 'name', 'Date', 'Result', 'Belligerents.allies', 'Belligerents.axis', 'Casualties and losses.allies', 'Casualties and losses.axis']
battles[columns].head(3)

msno.matrix(battles, labels=True, sparkline=False)
mask = battles[['Date', 'Location']].isnull().all(1)
battles.loc[mask, ['name', 'url']]

print(battles['Location'].iloc[10])

pattern = r'/ ([\d|\.]+); ([\d|\.]+)'

battles.head(10).Location.str.extract(pattern)
battles[['Latitude', 'Longitude']] = battles.Location.str.extract(pattern)
for col in 'Latitude', 'Longitude':
    battles[col] = battles[col].astype(float)