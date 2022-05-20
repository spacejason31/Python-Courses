algorithm = ['Linear Regression', 'Logistic Regression', 'RandomForest', 'a3c']
learning = ['Supervised', 'Supervised', 'Supervised', 'Reinforcement']
algorithm_type = ['Regression', 'Classification', 'Regression or Classification', 'Game AI']
algorithm.append('k-means')
learning.append('Unsupervised')
algorithm_type.append('Clustering')
machine_learning = {}
machine_learning['algorithm'] = algorithm
machine_learning['learning'] = learning
machine_learning['algorithm_type'] = algorithm_type
print(machine_learning)

#Using pandas to import various file types
import pandas as pd
pd.read_csv('https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter01/Dataset/csv_example.csv')
pd.read_excel('https://github.com/PacktWorkshops/The-Data-Science-Workshop/blob/master/Chapter01/Dataset/excel_example.xlsx?raw=true')
pd.read_json('https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter01/Dataset/json_example.json')

import pandas as pd
csv_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter01/Dataset/overall_topten_2012-2013.csv'
csv_df = pd.read_csv(csv_url, skiprows=1)
csv_df
tsv_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter01/Dataset/overall_topten_2012-2013.tsv'
tsv_df = pd.read_csv(tsv_url, skiprows=1 ,sep='\t')
tsv_df
xlsx_url = 'https://github.com/PacktWorkshops/The-Data-Science-Workshop/blob/master/Chapter01/Dataset/overall_topten_2012-2013.xlsx?raw=true'
xlsx_df = pd.read_excel(xlsx_url, skiprows=1, sheet_name=1)
xlsx_df

#Using sklearn to identify model trends
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(random_state=1)
from sklearn.datasets import load_wine
features, target = load_wine(return_X_y=True)
rf_model.fit(features, target)
preds = rf_model.predict(features)
preds
from sklearn.metrics import accuracy_score
accuracy_score(target, preds)

from sklearn.datasets import load_breast_cancer
features, target = load_breast_cancer(return_X_y=True)
print(features)
print(target)
from sklearn.ensemble import RandomForestClassifier
seed = 888
rf_model = RandomForestClassifier(random_state=seed)
rf_model.fit(features, target)
preds = rf_model.predict(features)
print(preds)
from sklearn.metrics import accuracy_score
accuracy_score(target, preds)

import pandas as pd
csv_loc = "dataset_44_spambase.csv"
csv_df = pd.read_csv(csv_loc)
print(csv_df)
target = csv_df.pop('class')
features = csv_df
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier()
rf_model.fit(features, target)
preds = rf_model.predict(features)
print(preds)
from sklearn.metrics import accuracy_score
accuracy_score(target, preds)