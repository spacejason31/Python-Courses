#Set up notebook & create the database for use throughout the document
%matplotlib inline
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.graphics.api as smg
import pandas as pd
import numpy as np
import patsy
from statsmodels.graphics.correlation import plot_corr
from sklearn.model_selection import train_test_split
plt.style.use('seaborn')
rawBostonData = pd.read_csv("Boston.csv")
rawBostonData.head()
rawBostonData = rawBostonData.dropna()
rawBostonData = rawBostonData.drop_duplicates()
list(rawBostonData)
renamedBostonData = rawBostonData.rename(columns={
    'CRIM': 'crimeRatePerCapita',
    ' ZN ': 'landOver25k_sqft',
    'INDUS ': 'nonRetailLandProptn',
    'CHAS': 'riverDummy',
    'NOX': 'nitrixOxide_pp10m',
    'RM': 'avgNoRoomsPerDwelling',
    'Age': 'proptnOwnerOccupied',
    'DIS':'weightedDist',
    'RAD':'radialHighwaysAccess',
    'TAX':'propTaxRate_per10K',
    'PTRATIO':'pupilTeacherRatio',
    'LSTAT':'pctLowerStatus',
    'MEDV':'medianValue_Ks'
})
renamedBostonData.head()
renamedBostonData.info()
renamedBostonData.describe(include=[np.number])
renamedBostonData.describe(include=[np.number]).T
X = renamedBostonData.drop('crimeRatePerCapita', axis=1)
y = renamedBostonData[['crimeRatePerCapita']]
seed=10
test_data_size = 0.3
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_data_size, random_state=seed)
train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

#Create heatmap for asociations between variables
corrMatrix = train_data.corr(method = 'pearson')
xnames = list(train_data.columns)
ynames = list(train_data.columns)
plot_corr(corrMatrix, xnames=xnames, ynames=ynames, title=None, normcolor=False, cmap='RdYlBu_r')

#Create a simple linear regression & scatterplot for 2 variables
fig, ax = plt.subplots(figsize=(10,6))
sns.regplot(x='medianValue_Ks', y='crimeRatePerCapita', ci=None, data=train_data, ax=ax, color='k', scatter_kws={"s": 20,"color":"royalblue", "alpha":1})
ax.set_ylabel('Crime rate per Capita', fontsize=15, fontname='DejaVu Sans')
ax.set_xlabel("Median value of owner-occupied, homes in $1000's", fontsize=15, fontname='DejaVu Sans')
ax.set_xlim(left=None, right=None)
ax.set_ylim(bottom=None, top=30)
ax.tick_params(axis='both', which='major', labelsize=12)
fig.tight_layout()

#Create a log-linear regression for 2 variables
fig, ax = plt.subplots(figsize=(10,6))
y = np.log(train_data['crimeRatePerCapita'])
sns.regplot(x='medianValue_Ks', y=y, ci=95, data=train_data, ax=ax, color='k', scatter_kws={"s": 20,"color":"royalblue", "alpha":1})
ax.set_ylabel('log of Crime rate per Capita', fontsize=15, fontname='DejaVu Sans')
ax.set_xlabel("Median value of owner-occupied, homes in $1000's", fontsize=15, fontname='DejaVu Sans')
ax.set_xlim(left=None, right=None)
ax.set_ylim(bottom=None, top=None)
ax.tick_params(axis='both', which='major', labelsize=12)
fig.tight_layout()

#Calculate Ordinary Least Squares (OLS) statistics for linear association between 2 variables
linearModel = smf.ols(formula='crimeRatePerCapita ~ medianValue_Ks', data=train_data)
linearModelResult = linearModel.fit()
print(linearModelResult.summary())
print(linearModelResult.conf_int())

#Calculate OLS statistics for log-linear association between 2 variables
loglinModel = smf.ols('np.log(crimeRatePerCapita) ~ medianValue_Ks', data=train_data)
loglinModelResult = loglinModel.fit()
print(loglinModelResult.summary())

loglinModel = smf.ols('np.log(crimeRatePerCapita) ~ nonRetailLandProptn', data=train_data)
loglinModelResult = loglinModel.fit()
print(loglinModelResult.summary())

#Calculate OLS statistics for multiple independent variables
multilinearModel = smf.ols(formula='crimeRatePerCapita ~ pctLowerStatus + radialHighwaysAccess + medianValue_Ks + nitrixOxide_pp10m', data=train_data)
multilinearResults = multilinearModel.fit()
print(multilinearResults.summary())
multilinearResults.rsquared

#Activity 2.02 fitting multi-log-linear regression model (with initial restrictions)
#Step 1: determine which variables & combinations have r^2 > 0.4
dep_variables = []
dep_var_rsq = {}
for variable1 in train_data.columns:
    for variable2 in train_data.columns:
        if variable1 != 'crimeRatePerCapita':
            if variable1 == variable2:
                formula = 'np.log(crimeRatePerCapita) ~ ' + variable1
                testModel = smf.ols(formula=formula, data=train_data)
                testResults = testModel.fit()
                if testResults.rsquared >= 0.4:
                    dep_variables.append(variable1)
                    dep_var_rsq[variable1] = testResults.rsquared
                    #print(variable1, 'r-sq = ', testResults.rsquared)
for variable1 in train_data.columns:
    for variable2 in train_data.columns:
        if (variable1 != 'crimeRatePerCapita') and (variable1 != variable2):
            if (str(variable2 + ':' + variable1) not in dep_variables):
                if (str(variable1) in dep_variables) and (str(variable2) in dep_variables):
                    formula = 'np.log(crimeRatePerCapita) ~ ' + variable1 + ':' + variable2
                    testModel = smf.ols(formula=formula, data=train_data)
                    testResults = testModel.fit()
                    if testResults.rsquared >= 0.4:
                        dep_variables.append(str(variable1 + ':' + variable2))
                        dep_var_rsq[str(variable1 + '*' + variable2)] = testResults.rsquared
                        #print(variable1, ':', variable2, 'r-sq = ', testResults.rsquared)
print(dep_var_rsq)
#Create formula string for those variables & create regression model
formula = 'np.log(crimeRatePerCapita) ~ '
for variable in dep_variables:
    if variable == dep_variables[0]:
        formula += variable
    else:
        formula += ' + '
        formula += variable
multiModel = smf.ols(formula=formula, data=train_data)
multiResults = multiModel.fit()
print(multiResults.summary())

#Alternative method - building up to r^2 >= 0.8 using highest r^2 values
#Create lists & dictionary for...
dep_variables = []              #All single variables
dep_var_all = []                #All variables (single+combi)
dep_var_rsq = {}                #All variables & r^2 values
for variable1 in train_data.columns:
    for variable2 in train_data.columns:
        if variable1 != 'crimeRatePerCapita':
            if variable1 == variable2:
                formula = 'np.log(crimeRatePerCapita) ~ ' + variable1
                testModel = smf.ols(formula=formula, data=train_data)
                testResults = testModel.fit()
                dep_variables.append(variable1)
                dep_var_all.append(variable1)
                dep_var_rsq[variable1] = testResults.rsquared
            elif (variable1 != variable2):
                if (str(variable2 + ':' + variable1) not in dep_var_all):
                    formula = 'np.log(crimeRatePerCapita) ~ ' + variable1 + ':' + variable2
                    testModel = smf.ols(formula=formula, data=train_data)
                    testResults = testModel.fit()
                    dep_var_all.append(str(variable1 + ':' + variable2))
                    dep_var_rsq[str(variable1 + ':' + variable2)] = testResults.rsquared
#Order all variables by r^2 value
rsq_sorted = sorted(dep_var_rsq.items(), key=lambda x: x[1], reverse=True)
#Create lists (single & single+combi) of variables in order of r^2 value: highest to lowest
depvarall_sorted = [variable[0] for variable in rsq_sorted]     #Single+combi
depvar_sorted = []                                              #Single
for name in depvarall_sorted:
    if name in dep_variables:
        depvar_sorted.append(name)

#Build up regression model from variables (H->L) until r^2 >=0.8