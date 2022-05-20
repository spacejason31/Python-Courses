import pandas as pd
df = pd.read_csv("activity.csv")
df.head()
from sklearn.model_selection import train_test_split
target=df.pop('Activity')
X_train, X_test, y_train, y_test = train_test_split(df, target, test_size=0.33, random_state=42)
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(random_state=1, n_estimators=10)
rf_model.fit(X_train, y_train)
preds = rf_model.predict(X_train)
preds
from sklearn.metrics import accuracy_score
accuracy_score(y_train, preds)
test_preds = rf_model.predict(X_test)
accuracy_score(y_test, test_preds)

#Exercise 4.01
import pandas as pd
df = pd.read_csv("openml_phpZNNasq.csv")
df.head()
df.drop(columns='animal', inplace=True)
y=df.pop('type')
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.4, random_state=188)
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(random_state=42, n_estimators=10)
rf_model.fit(X_train, y_train)
train_preds = rf_model.predict(X_train)
train_preds
from sklearn.metrics import accuracy_score
train_acc = accuracy_score(y_train, train_preds)
train_acc
test_preds = rf_model.predict(X_test)
test_acc = accuracy_score(y_test, test_preds)
test_acc

rf_model2 = RandomForestClassifier(random_state=1, n_estimators=50)
rf_model2.fit(X_train, y_train)
preds2 = rf_model2.predict(X_train)
test_preds2 = rf_model2.predict(X_test)
print(accuracy_score(y_train, preds2))
print(accuracy_score(y_test, test_preds2))

rf_model3 = RandomForestClassifier(random_state=1, n_estimators=50)
rf_model3.fit(X_train, y_train)
preds3 = rf_model3.predict(X_train)
test_preds3 = rf_model3.predict(X_test)
print(accuracy_score(y_train, preds3))
print(accuracy_score(y_test, test_preds3))

#Exercise 4.02
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv("openml_phpZNNasq.csv")
df.drop(columns='animal', inplace=True)
y=df.pop('type')
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.4, random_state=188)
rf_model = RandomForestClassifier(random_state=42, n_estimators=1)
rf_model.fit(X_train, y_train)
train_preds = rf_model.predict(X_train)
test_preds = rf_model.predict(X_test)
print(accuracy_score(y_train, train_preds))
print(accuracy_score(y_test, test_preds))
rf_model2 = RandomForestClassifier(random_state=42, n_estimators=30)
rf_model2.fit(X_train, y_train)
train_preds2 = rf_model2.predict(X_train)
test_preds2 = rf_model2.predict(X_test)
print(accuracy_score(y_train, train_preds2))
print(accuracy_score(y_test, test_preds2))
rf_model4 = RandomForestClassifier(random_state=1, n_estimators=50, max_depth=3)
rf_model4.fit(X_train, y_train)
preds4 = rf_model4.predict(X_train)
test_preds4 = rf_model4.predict(X_test)
print(accuracy_score(y_train, preds4))
print(accuracy_score(y_test, test_preds4))
rf_model5 = RandomForestClassifier(random_state=1, n_estimators=50, max_depth=10)
rf_model5.fit(X_train, y_train)
preds5 = rf_model5.predict(X_train)
test_preds5 = rf_model5.predict(X_test)
print(accuracy_score(y_train, preds5))
print(accuracy_score(y_test, test_preds5))
rf_model6 = RandomForestClassifier(random_state=1, n_estimators=50, max_depth=50)
rf_model6.fit(X_train, y_train)
preds6 = rf_model6.predict(X_train)
test_preds6 = rf_model6.predict(X_test)
print(accuracy_score(y_train, preds6))
print(accuracy_score(y_test, test_preds6))

#Exercise 4.03
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv("openml_phpZNNasq.csv")
df.drop(columns='animal', inplace=True)
y = df.pop('type')
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.4, random_state=188)
rf_model = RandomForestClassifier(random_state=42, n_estimators=30, max_depth=5)
rf_model.fit(X_train, y_train)
train_preds = rf_model.predict(X_train)
test_preds = rf_model.predict(X_test)
print(accuracy_score(y_train, train_preds))
print(accuracy_score(y_test, test_preds))
rf_model2 = RandomForestClassifier(random_state=42, n_estimators=30, max_depth=2)
rf_model2.fit(X_train, y_train)
train_preds2 = rf_model2.predict(X_train)
test_preds2 = rf_model2.predict(X_test)
print(accuracy_score(y_train, train_preds2))
print(accuracy_score(y_test, test_preds2))

rf_model7 = RandomForestClassifier(random_state=1, n_estimators=50, max_depth=10, min_samples_leaf=3)
rf_model7.fit(X_train, y_train)
preds7 = rf_model7.predict(X_train)
test_preds7 = rf_model7.predict(X_test)
print(accuracy_score(y_train, preds7))
print(accuracy_score(y_test, test_preds7))

rf_model8 = RandomForestClassifier(random_state=1, n_estimators=50, max_depth=10, min_samples_leaf=10)
rf_model8.fit(X_train, y_train)
preds8 = rf_model7.predict(X_train)
test_preds8 = rf_model8.predict(X_test)
print(accuracy_score(y_train, preds8))
print(accuracy_score(y_test, test_preds8))

#Activity 4.01
import pandas as pd
df = pd.read_csv("phpB0xrNj.csv")
df.head()
y = df.pop('class')
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.3)
def tester(n_est, depth, samples, features):
    rf_model = RandomForestClassifier(n_estimators=n_est, max_depth=depth, min_samples_leaf=samples, max_features=features)
    rf_model.fit(X_train, y_train)
    preds = rf_model.predict(X_train)
    test_preds = rf_model.predict(X_test)
    train_score = accuracy_score(y_train, preds)
    test_score = accuracy_score(y_test, test_preds)
    print("n_estimator:", n_est, "\nmax_depth:", depth, "\nmin_samples_leaf:", samples, "\nmax_features:", features, "\ntraining accuracy:", train_score, "\ntesting accuracy:", test_score)
#round 1
tester(20, 5, 10, 0.5)
tester(50, 5, 10, 0.5)
tester(20, 10, 10, 0.5) #best so far
tester(20, 5, 50, 0.5)
tester(20, 5, 10, 0.3)
#round 2
tester(20, 10, 10, 0.3)
tester(50, 10, 10, 0.3)
tester(20, 8, 20, 0.3)
tester(20, 8, 20, 0.2) #best
tester(20, 12, 20, 0.2)