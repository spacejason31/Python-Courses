temperature = 23
temp_1 = 23
temp_2 = 24
temp_3 = 23
temp_4 = 22
temp_5 = 22
temps_list = [23,24,23,22,22]
import numpy as np
temps_ndarray = np.array(temps_list)
print(type(temps_ndarray))
print(temps_ndarray.shape)
print(temps_list)

temps_matrix = temps_ndarray.reshape(-1,1)
print(temps_matrix.shape)
print(temps_matrix.reshape(1,5))

# Exercise 6.02 Computing r2 score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures

_headers = ['CIC0','SM!','GATS1i','NdsCH','Ndssc','MLOGP','response']
df = pd.read_csv('https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter06/Dataset/qsar_fish_toxicity.csv', names=_headers, sep=";")

features = df.drop('response', axis=1).values
labels = df[['response']].values
X_train, X_eval, y_train, y_eval = train_test_split(features, labels, test_size=0.2, random_state=0)
X_val, X_test, y_val, y_test = train_test_split(X_eval, y_eval, random_state=0)
steps = [('scaler', MinMaxScaler()),
        ('poly', PolynomialFeatures(2)),
        ('model', LinearRegression())]
model = Pipeline(steps)
model.fit(X_train, y_train)
y_pred = model.predict(X_val)
mae = mean_absolute_error(y_val, y_pred)
print('MAE: {}'.format(mae))
r2 = model.score(X_val, y_val)
print('R^2 score: {}'.format(r2))

# Exercise 6.05 Classification Model for Computing Ecaluation Metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

_headers = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'car']
df = pd.read_csv("https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter06/Dataset/car.data", names=_headers, index_col=None)
df.head()

_df = pd.get_dummies(df, columns=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])
_df.head()

features = _df.drop('car', axis=1).values
labels = _df['car'].values
X_train, X_eval, y_train, y_eval = train_test_split(features, labels, test_size = 0.3, random_state=0)
X_val, X_test, y_val, y_test = train_test_split(X_eval, y_eval, test_size=0.5, random_state=0)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_val)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_val, y_pred)

#6.07-6.11 Computing Precision, Recall, F1 Score, Accuracy, Log Loss
from sklearn.metrics import precision_score
precision_score(y_val, y_pred, average='macro') # true positives/all positive predictions
from sklearn.metrics import recall_score
recall_score(y_val, y_pred, average='macro')    # true predictions/all true cases (aka sensitivity)
from sklearn.metrics import f1_score
f1_score(y_val, y_pred, average='macro')        # 2*(precision*recall)/(precision+recall)
from sklearn.metrics import accuracy_score
_accuracy = accuracy_score(y_val, y_pred)       # (true positives+true negatives)/total population
print(_accuracy)
from sklearn.metrics import log_loss
log_loss(y_val, model.predict_proba(X_val))     # the negative log-likelihood of the true values given your model predictions

#6.12 Computing/Plotting ROC Curve
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve
from sklearn.metrics import auc

_headers = ['Age', 'Delivery_Nbr', 'Delivery_Time', 'Blood_Pressure', 'Heart_Problem', 'Caesarian']
df = pd.read_csv("https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter06/Dataset/caesarian.csv.arff", names=_headers, index_col=None, skiprows=15)
df.head()

features = df.drop(['Caesarian'], axis=1).values
labels = df[['Caesarian']].values
X_train, X_eval, y_train, y_eval = train_test_split(features, labels, test_size=0.2, random_state=0)
X_val, X_test, y_val, y_test = train_test_split(X_eval, y_eval, test_size=0.5, random_state=0)
model = LogisticRegression()
model.fit(X_train, y_train)
y_proba = model.predict_proba(X_val)
_false_positive, _true_positive, _thresholds = roc_curve(y_val, y_proba[:, 0])
print(_false_positive)
print(_true_positive)
print(_thresholds)

import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(_false_positive, _true_positive, lw=2, label = 'Receiver Operating Characteristic')
plt.xlim(0.0, 1.2)
plt.ylim(0.0, 1.2)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.show()

y_proba = model.predict_proba(X_val)
from sklearn.metrics import roc_auc_score
_auc = roc_auc_score(y_val, y_proba[:, 0])
print(_auc)

#6.14 Saving and Loading a Model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

_headers = ['CIC0', 'SM1', 'GATS1i', 'NdsCH', 'Ndssc', 'MLOGP', 'response']
df = pd.read_csv('https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter06/Dataset/qsar_fish_toxicity.csv', names=_headers, sep=';')
df.head()

features = df.drop('response', axis=1).values
labels = df[['response']].values
X_train, X_eval, y_train, y_eval = train_test_split(features, labels, test_size=0.2, random_state=0)
X_val, X_test, y_val, y_test = train_test_split(X_eval, y_eval, random_state=0)

model = LinearRegression()
print(model)
model.fit(X_train, y_train)
y_pred = model.predict(X_val)

import joblib
joblib.dump(model, './model.joblib')
m2 = joblib.load('./model.joblib')
m2_preds = m2.predict(X_val)
ys = pd.DataFrame(dict(predicted=y_pred.reshape(-1), m2=m2_preds.reshape(-1)))
ys.head()