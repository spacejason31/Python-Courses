#Exercise 3.01
import pandas as pd
bankData = pd.read_csv("bank-full.csv", sep = ';')
bankData.head()
print(bankData.shape)
bankData.describe()

import matplotlib.pyplot as plt
import numpy as np
jobList = ['admin', 'scientist', 'doctor', 'management']
jobYes = [20,60,70,40]
jobNo = [80, 40, 30, 60]
xlabels = len(jobList)
ind = np.arange(xlabels)
width = 0.35
p1 = plt.bar(ind, jobYes, width)
p2 = plt.bar(ind, jobNo, width, bottom=jobYes)
plt.ylabel('Proportion of Jobs')
plt.title('Job')
plt.xticks(ind, jobList)
plt.yticks(np.arange(0, 101, 10))
plt.legend((p1[0], p2[0]), ('Yes', 'No'))
plt.xticks(rotation=60)
plt.show()

#Exercise 3.02
import altair as alt
filter_mask = bankData['y'] == 'yes'
bankSub1 = bankData[filter_mask].groupby('age')['y'].agg(agegrp='count').reset_index()
alt.Chart(bankSub1).mark_point().encode(x='age', y='agegrp')    #Print this step to get a dot graph
alt.Chart(bankSub1).mark_line().encode(x='age', y='agegrp')     #Print this step to get a line graph
ageTot = bankData.groupby('age')['y'].agg(ageTot='count').reset_index()
ageTot.head()
ageProp = bankData.groupby(['age', 'y'])['y'].agg(ageCat='count').reset_index()
ageProp.head()
ageComb = pd.merge(ageProp, ageTot, left_on=['age'], right_on=['age'])
ageComb['catProp'] = (ageComb.ageCat/ageComb.ageTot)*100
ageComb.head()
alt.Chart(ageComb).mark_line().encode(x='age', y='catProp').facet(column='y')

#Activity 3.01
bankData.head()
jobTot = bankData.groupby('job')['y'].agg(jobTot='count').reset_index()
jobTot.head()
jobProp = bankData.groupby(['job','y'])['y'].agg(jobCat='count').reset_index()
jobProp.head()
jobComb = pd.merge(jobTot, jobProp, left_on=['job'], right_on=['job'])
jobComb['catProp'] = (jobComb.jobCat/jobComb.jobTot)*100
jobComb.head()
alt.Chart(jobComb).mark_bar().encode(x='job', y='catProp', color='y')

#Exercise 3.03
bankData.groupby(['housing', 'y'])['y'].agg(houseTot='count').reset_index()
bankData.groupby(['loan', 'y'])['y'].agg(loanTot='count').reset_index()
import numpy as np
np.quantile(bankData['balance'],[0.25,0.5,0.75])
bankData['balanceClass'] = 'Quant1'
bankData.loc[(bankData['balance']>72) & (bankData['balance']<448), 'balanceClass'] = 'Quant2'
bankData.loc[(bankData['balance']>448) & (bankData['balance']<1428), 'balanceClass'] = 'Quant3'
bankData.loc[(bankData['balance']>1428), 'balanceClass'] = 'Quant4'
bankData.head()
balanceTot = bankData.groupby(['balanceClass'])['y'].agg(balanceTot='count').reset_index()
balanceTot
balanceProp = bankData.groupby(['balanceClass', 'y'])['y'].agg(balanceCat='count').reset_index()
balanceProp
balanceComb = pd.merge(balanceProp, balanceTot, on=['balanceClass'])
balanceComb['catProp'] = (balanceComb.balanceCat/balanceComb.balanceTot)*100

#Exercise 3.04
import pandas as pd
import numpy as np
bankData = pd.read_csv("bank-full.csv", sep=";")
from sklearn import preprocessing
x = bankData[['balance']].values.astype(float)
minmaxScalar = preprocessing.MinMaxScaler()
bankData['balanceTran'] = minmaxScalar.fit_transform(x)
bankData['balanceTran'] += 0.00001
bankData['loanTran'] = 1
bankData.loc[bankData['loan']=='no', 'loanTran'] = 5
bankData['houseTran'] = 5
bankData.loc[bankData['housing']=='no', 'houseTran'] = 1
bankData['assetIndex'] = bankData['balanceTran']*bankData['loanTran']*bankData['houseTran']
bankData.head(n=10)
bankData['assetIndex'].describe()
np.quantile(bankData['assetIndex'], [0.25,0.50,0.75])
bankData['assetClass'] = 'Quant1'
bankData.loc[(bankData['assetIndex']>0.37668646) & (bankData['assetIndex']<=0.56920367), 'assetClass'] = 'Quant2'
bankData.loc[(bankData['assetIndex']>0.56920367) & (bankData['assetIndex']<=1.9027249), 'assetClass'] = 'Quant3'
bankData.loc[(bankData['assetIndex']>1.9027249), 'assetClass'] = 'Quant4'
bankData.head()
assetTot = bankData.groupby('assetClass')['y'].agg(assetTot='count').reset_index()
assetProp = bankData.groupby(['assetClass', 'y'])['y'].agg(assetCat='count').reset_index()
assetComb = pd.merge(assetTot, assetProp, on=['assetClass'])
assetComb['catProp'] = (assetComb.assetCat / assetComb.assetTot)*100
assetComb
import altair as alt
alt.Chart(assetComb).mark_bar().encode(x='assetClass', y='catProp', color='y')

#additional exploring of quantile 2
quant2 = bankData.loc[bankData['assetClass']=='Quant2']
#Function that created new variable with quantile descriptors
def quartiler(dataset, input_var, new_var):
    quant = np.quantile(dataset[str(input_var)], [0.25,0.50,0.75])
    dataset[str(new_var)] = 'Quant1'
    dataset.loc[(dataset[str(input_var)]>quant[0]) & (dataset[str(input_var)]<quant[1]), str(new_var)] = 'Quant2'
    dataset.loc[(dataset[str(input_var)]>quant[1]) & (dataset[str(input_var)]<=quant[2]), str(new_var)] = 'Quant3'
    dataset.loc[(dataset[str(input_var)]>quant[2]), str(new_var)] = 'Quant4'
    return quant
quartiler(bankData, "balance", "balanceClass")

#Exercise 3.05
import pandas as pd
from pandas import set_option
bankNumeric = bankData[['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous', 'balanceTran', 'loanTran', 'houseTran', 'assetIndex']]
set_option('display.width', 150)
set_option('precision',3)
bankCorr = bankNumeric.corr(method='pearson')
bankCorr
from matplotlib import pyplot as plt
corFig = plt.figure()
figAxis = corFig.add_subplot(111)
corAx = figAxis.matshow(bankCorr, vmin=-1, vmax=1)
corFig.colorbar(corAx)
plt.show()
bankNumeric.skew()
#Histograms
fig, axs = plt.subplots(1,2)
axs[0].hist(bankNumeric['age'])
axs[0].set_title("Distribution of age")
axs[1].hist(bankNumeric['assetIndex'])
axs[1].set_title("Distribution of asset index")
#Density plots
bankNumeric['age'].plot(kind='density', subplots=False, layout=(1,1))
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Normalised Age Distribution")
plt.show()

from sklearn.preprocessing import StandardScaler
from numpy import set_printoptions
scaling = StandardScaler().fit(bankNumeric)
rescaledNum = scaling.transform(bankNumeric)
set_printoptions(precision=3)
rescaledNum
from sklearn.preprocessing import Normalizer
normaliser = Normalizer().fit(bankNumeric)
normalisedNum = normaliser.transform(bankNumeric)
set_printoptions(precision=3)
normalisedNum
normFig = plt.figure()
figAxis = normFig.add_subplot(111)
normAx = figAxis.matshow(normalisedNum, vmin=-1, vmax=1)
normFig.colorbar(normAx)
plt.show()

normPlot = pd.DataFrame(data=normalisedNum, columns=['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous', 'balanceTran', 'loanTran', 'houseTran', 'assetIndex'])
set_option('display.width', 150)
set_option('precision',3)
normCorr = normPlot.corr(method='pearson')
normCorr
normFig = plt.figure()
figAxis = normFig.add_subplot(111)
normAx = figAxis.matshow(normCorr, vmin=-1, vmax=1)
normFig.colorbar(normAx)
plt.show()
import seaborn as sns
plt.figure(figsize=(10,6))
sns.heatmap(normCorr, annot=True, vmin=-1, vmax=1, fmt=".3f", linewidths=2, cmap="PRGn")

#Exercise 3.06
import pandas as pd
import altair as alt
bankData = pd.read_csv("bank-full.csv", sep = ';')
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
bankData.dtypes
bankCat = pd.get_dummies(bankData[['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']])
bankCat.shape
bankNum = bankData[['age','balance','day','duration','campaign','pdays','previous']]
bankNum.shape
X = pd.concat([bankCat, bankNum], axis=1)
Y = bankData['y']
print(X.shape, Y.shape)
X.head()
Y.head()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=123)
bankModel = LogisticRegression()
bankModel.fit(X_train, Y_train)
pred = bankModel.predict(X_test)
print("Accuracy of Logistic regression model prediction on test set: {:.2f}".format(bankModel.score(X_test, Y_test)))
from sklearn.metrics import confusion_matrix
confusionMatrix = confusion_matrix(Y_test, pred)
print(confusionMatrix)
from sklearn.metrics import classification_report
print(classification_report(Y_test, pred))

#Activity 3.02
bankCat = pd.get_dummies(bankData[['job','marital','education','default','contact','month','poutcome']])
bankNum = bankData[['age','day','previous','balanceTran','loanTran','houseTran','assetIndex','durationTran','campaignTran','pdaysTran']]

import seaborn as sns
#transform variables: duration, campaign, pdays
sns.distplot(bankData.age)
sns.distplot(bankData.day)
sns.distplot(bankData.duration)
sns.distplot(bankData.campaign)
sns.distplot(bankData.pdays)
sns.distplot(bankData.previous)

from sklearn import preprocessing
def normalizer(var, new_var, dataset=bankData):
    x = dataset[[var]].values.astype(float)
    dataset[new_var] = preprocessing.MinMaxScaler().fit_transform(x)
    dataset[new_var] += 0.00001
normalizer("duration", "durationTran")
normalizer('campaign', 'campaignTran')
normalizer('pdays', 'pdaysTran')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
X = pd.concat([bankCat, bankNum], axis=1)
Y = bankData['y']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
bankModel = LogisticRegression()
bankModel.fit(X_train, y_train)
pred = bankModel.predict(X_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
print("Accuracy of Logistic regression model prediction on test set: {:.2f}".format(bankModel.score(X_test, y_test)))
confusionMatrix = confusion_matrix(y_test, pred)
print(confusionMatrix)
print(classification_report(y_test, pred))