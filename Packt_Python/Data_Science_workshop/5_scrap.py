#Exercise 5.01
import pandas as pd
from sklearn.cluster import KMeans
df = pd.read_csv("taxstats2015.csv", usecols=['Postcode', 'Average net tax', 'Average total deductions'])
kmeans = KMeans(random_state=42)
X = df[['Average net tax', 'Average total deductions']]
kmeans.fit(X)
y_preds = kmeans.predict(X)
y_preds
df['cluster'] = y_preds
df.head()
import numpy as np
df.pivot_table(values=['Average net tax', 'Average total deductions'], index='cluster', aggfunc=np.mean)
import altair as alt
alt.Chart(df).mark_circle().encode(x='Average net tax', y='Average total deductions', color='cluster:N', tooltip=['Postcode', 'cluster', 'Average net tax', 'Average total deductions']).interactive()

clusters = pd.DataFrame()
clusters['cluster_range'] = range(1,10)
inertia = []
for k in clusters['cluster_range']:
    kmeans = KMeans(n_clusters=k, random_state=8).fit(X)
    inertia.append(kmeans.inertia_)
clusters['inertia'] = inertia
clusters
alt.Chart(clusters).mark_line().encode(x='cluster_range', y='inertia')

kmeans = KMeans(random_state=42, n_clusters=3).fit(X)
df['cluster2'] = kmeans.predict(X)
alt.Chart(df).mark_circle().encode(x='Average net tax', y='Average total deductions', color='cluster2:N', tooltip=['Postcode', 'cluster2', 'Average net tax', 'Average total deductions']).interactive()

kmeans = KMeans(random_state=14, n_clusters=3, init='random', n_init=1).fit(X)
df['cluster3'] = kmeans.predict(X)
alt.Chart(df).mark_circle().encode(x='Average net tax', y='Average total deductions', color='cluster3:N', tooltip=['Postcode', 'cluster3', 'Average net tax', 'Average total deductions']).interactive()

kmeans = KMeans(random_state=14, n_clusters=3, init='k-means++', n_init=5).fit(X)
df['cluster4'] = kmeans.predict(X)
alt.Chart(df).mark_circle().encode(x='Average net tax', y='Average total deductions', color='cluster4:N', tooltip=['Postcode', 'cluster4', 'Average net tax', 'Average total deductions']).interactive()


#Exercise 5.02
import pandas as pd
from sklearn.cluster import KMeans
import altair as alt
import numpy as np
df = pd.read_csv("taxstats2015.csv", usecols=['Postcode', 'Average total business income', 'Average total business expenses'])
df.tail(10)
X = df[['Average total business income', 'Average total business expenses']]
kmeans = KMeans(random_state=8)
kmeans.fit(X)
y_preds = kmeans.predict(X)
y_preds[-10:]
df['cluster'] = y_preds
df.tail(10)

#Exercise 5.03
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import altair as alt
df = pd.read_csv("taxstats2015.csv", usecols=['Postcode', 'Average total business income', 'Average total business expenses'])
df.head()
X = df[['Average total business income', 'Average total business expenses']]
clusters = pd.DataFrame()
inertia = []
clusters['cluster_range'] = range(1,15)
for k in clusters['cluster_range']:
    kmeans = KMeans(n_clusters=k).fit(X)
    inertia.append(kmeans.inertia_)
clusters['inertia'] = inertia
clusters
alt.Chart(clusters).mark_line().encode(x='cluster_range', y='inertia')
optim_cluster=4
kmeans = KMeans(random_state=42, n_clusters=optim_cluster)
kmeans.fit(X)
df['cluster2'] = kmeans.predict(X)
df.head(10)
alt.Chart(df).mark_circle().encode(x='Average total business income', y='Average total business expenses', color='cluster2:N', tooltip=['Postcode', 'cluster2', 'Average total business income', 'Average total business expenses']).interactive()

#Exercise 5.04
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import altair as alt
df = pd.read_csv("taxstats2015.csv", usecols=['Postcode', 'Average total business income', 'Average total business expenses'])
X = df[['Average total business income', 'Average total business expenses']]

x = X.iloc[0,].values
y = X.iloc[1,].values
print(x)
print(y)

sq_euclidean = (x[0] - y[0])**2 + (x[1] - y[1])**2

sqs = []
for i in range(len(X)):
    diff = X.iloc[i,0] - X.iloc[i,1]
    sqs.append(diff**2)

kmeans = KMeans(random_state=42, n_clusters=3, init='k-means++', n_init=5)
kmeans.fit(X)
df['cluster6'] = kmeans.predict(X)
centroids = kmeans.cluster_centers_
centroids = pd.DataFrame(centroids, columns=['Average net tax', 'Average total deductions'])
print(centroids)

chart1 = alt.Chart(df).mark_circle().encode(x='Average net tax', y='Average total deductions', color='cluster6:N', tooltip=['Postcode', 'cluster6', 'Average net tax', 'Average total deductions']).interactive()
chart1
chart2 = alt.Chart(centroids).mark_circle(size=100).encode(x='Average net tax', y='Average total deductions', color=alt.value('black'), tooltip=['Average net tax', 'Average total deductions']).interactive()
chart2
chart1 + chart2

#Exercise 5.05
import pandas as pd
from sklearn.cluster import KMeans
import altair as alt
df = pd.read_csv("taxstats2015.csv", usecols=['Postcode', 'Average total business income', 'Average total business expenses'])
X = df[['Average total business income', 'Average total business expenses']]
income_min = df['Average total business income'].min()
income_max = df['Average total business income'].max()
expenses_min = df['Average total business expenses'].min()
expenses_max = df['Average total business expenses'].max()
print(income_min, "\n", income_max, "\n", expenses_min, "\n", expenses_max)
import random
random.seed(42)
centroids = pd.DataFrame()
centroids['Average total business income'] = random.sample(range(income_min, income_max), 4)
centroids['Average total business expenses'] = random.sample(range(expenses_min, expenses_max), 4)
centroids['cluster'] = centroids.index
centroids
chart1 = alt.Chart(df.head()).mark_circle().encode(x='Average total business income', y='Average total business expenses', color=alt.value('orange'), tooltip=['Postcode', 'Average total business income', 'Average total business expenses']).interactive()
chart2 = alt.Chart(centroids).mark_circle(size=100).encode(x='Average total business income', y='Average total business expenses', color=alt.value('black'), tooltip=['cluster', 'Average total business income', 'Average total business expenses']).interactive()
chart1 + chart2
def squared_euclidean(data_x, data_y, centroid_x, centroid_y, ):
    return (data_x - centroid_x)**2 + (data_y - centroid_y)**2
data_x = df.at[0, 'Average total business income']
data_y = df.at[0, 'Average total business expenses']
distances = [squared_euclidean(data_x, data_y, centroids.at[i, 'Average total business income'], centroids.at[i, 'Average total business expenses']) for i in range(4)]
distances
cluster_index = distances.index(min(distances))
df.at[0, 'cluster'] = cluster_index
df.head()

for j in range(5):
    data_x = df.at[j, 'Average total business income']
    data_y = df.at[j, 'Average total business expenses']
    distances = [squared_euclidean(data_x, data_y, centroids.at[i, 'Average total business income'], centroids.at[i, 'Average total business expenses']) for i in range(4)]
    distances
    cluster_index = distances.index(min(distances))
    df.at[j, 'cluster'] = cluster_index
df.head()

chart1 = alt.Chart(df.head()).mark_circle().encode(x='Average total business income', y='Average total business expenses', color='cluster:N', tooltip=['Postcode', 'cluster', 'Average total business income', 'Average total business expenses']).interactive()
chart2 = alt.Chart(centroids).mark_circle(size=100).encode(x='Average total business income', y='Average total business expenses', color=alt.value('black'), tooltip=['cluster', 'Average total business income', 'Average total business expenses']).interactive()
chart1 + chart2

for j in range(len(df)):
    data_x = df.at[j, 'Average total business income']
    data_y = df.at[j, 'Average total business expenses']
    distances = [squared_euclidean(data_x, data_y, centroids.at[i, 'Average total business income'], centroids.at[i, 'Average total business expenses']) for i in range(4)]
    distances
    cluster_index = distances.index(min(distances))
    df.at[j, 'cluster'] = cluster_index

from sklearn.preprocessing import MinMaxScaler
min_max_scalar = MinMaxScaler()
min_max_scalar.fit(X)
X_min_max = min_max_scalar.transform(X)
X_min_max
X_min_max[:,0].min(), X_min_max[:,0].max(), X_min_max[:,1].min(), X_min_max[:,1].max()
from sklearn.preprocessing import StandardScaler
standard_scaler = StandardScaler()
X_scaled = standard_scaler.fit_transform(X)
X_scaled
X_scaled[:,0].min(), X_scaled[:,0].max(), X_scaled[:,1].min(), X_scaled[:,1].max()

kmeans = KMeans(random_state=42, n_clusters=3, init='k-means++', n_init=5)
kmeans.fit(X_scaled)
df['cluster7'] = kmeans.predict(X_scaled)
alt.Chart(df).mark_circle().encode(x='Average net tax', y='Average total deductions', color='cluster7:N', tooltip=['Postcode', 'cluster7', 'Average net tax', 'Average total deductions']).interactive()

#Exercies 5.06
import pandas as pd
from sklearn.cluster import KMeans
import altair as alt
df = pd.read_csv("taxstats2015.csv", usecols=['Postcode', 'Average total business income', 'Average total business expenses'])
X = df[['Average total business income', 'Average total business expenses']]
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X)
X_min_max = min_max_scaler.transform(X)
X_min_max
kmeans = KMeans(random_state=1, n_clusters=4, init='k-means++', n_init=5)
kmeans.fit(X_min_max)
df['cluster8'] = kmeans.predict(X_min_max)
scatter_plot = alt.Chart(df).mark_circle().encode(x='Average total business income', y='Average total business expenses', color='cluster8:N', tooltip=['Postcode', 'cluster8', 'Average total business income', 'Average total business expenses']).interactive()
standard_scaler = StandardScaler()
X_scaled = standard_scaler.fit_transform(X)
kmeans = KMeans(random_state=1, n_clusters=4, init='k-means++', n_init=5)
kmeans.fit(X_scaled)
df['cluster9'] = kmeans.predict(X_scaled)
scatter_plot = alt.Chart(df).mark_circle().encode(x='Average total business income', y='Average total business expenses', color='cluster9:N', tooltip=['Postcode', 'cluster9', 'Average total business income', 'Average total business expenses']).interactive()

#Activity 5.01
import pandas as pd
import altair as alt
df = pd.read_csv("german.data-numeric", header=None, sep='\s\s+', prefix='X')
X = df[['X3', 'X9']]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
scaled = scaler.transform(X)

from sklearn.cluster import KMeans
clusters = pd.DataFrame()
clusters['cluster_range'] = range(1,10)
inertia = []
for k in clusters['cluster_range']:
    kmeans = KMeans(n_clusters=k, random_state=8).fit(scaled)
    inertia.append(kmeans.inertia_)
clusters['inertia'] = inertia
clusters
alt.Chart(clusters).mark_line().encode(x='cluster_range', y='inertia')

#lets go with 5 clusters
kmeans = KMeans(n_clusters = 5, init='k-means++', n_init=50, max_iter=1000)
kmeans.fit(scaled)
X['cluster5'] = kmeans.predict(scaled)
alt.Chart(X).mark_circle().encode(x='X3', y='X9', color='cluster5:N', tooltip=['X3', 'X9', 'cluster5']).interactive()

#not as good with 4 clusters (stick with 5 clusters)
kmeans4 = KMeans(n_clusters=4, init='k-means++', n_init=50, max_iter=1000)
kmeans4.fit(scaled)
X['cluster4'] = kmeans4.predict(scaled)
alt.Chart(X).mark_circle().encode(x='X3', y='X9', color='cluster4:N', tooltip=['X3', 'X9', 'cluster4']).interactive()