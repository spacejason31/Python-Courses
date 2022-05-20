# Import pandas library
import pandas as pd

# Create dataframe
sample_data = {'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
               'gender': ['M', 'F', 'F', 'M', 'M'],
               'communication_skill_score': [40, 45, 23, 39, 39],
               'quantitative_skill_score': [38, 41, 42, 48, 32]}

data = pd.DataFrame(sample_data, columns = ['name', 'gender', 'communication_skill_score', 'quantitative_skill_score'])
data.head()

data['quantitative_skill_score'].mean(axis=0)
data['communication_skill_score'].mode()
data['communication_skill_score'].median()
data.plot.hist()

df = pd.read_csv('Data_Analysis_3e\Chapter05\HR_comma_sep.csv')
df.head()
df.describe()
df['satisfaction_level'].plot.hist()
import seaborn as sns
sns.histplot(data = df, x = 'satisfaction_level', hue = 'left')

import altair as alt
import seaborn as sns
import pandas as pd

dat = pd.read_csv('Data_Analysis_3e\Chapter05\HR_comma_sep.csv')
df = pd.DataFrame(dat)
df.head()

sns.displot(df, x = 'satisfaction_level', aspect = 1.5)
alt.Chart(df).mark_bar().encode(
    alt.X('satisfaction_level', bin=False), y='count()'
).properties(height=300, width=450)
alt.data_transformers.disable_max_rows()
