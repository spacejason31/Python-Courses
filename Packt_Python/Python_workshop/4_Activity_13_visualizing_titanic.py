#Visualizing the Titanic dataset
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
lines = []
with open('titanic_train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        lines.append(line)

data = lines[1:]
passengers = []
headers = lines[0]

for d in data:
    p = {}
    for i in range(0, len(headers)):
        key = headers[i]
        value = d[i]
        p[key] = value
    passengers.append(p)

survived = [p['Survived'] for p in passengers]
pclass = [p['Pclass'] for p in passengers]
age = [float(p['Age']) for p in passengers if p['Age'] != '']
gender_survived = [p['Sex'] for p in passengers if int(p['Survived']) == 1]
gender_died = [p['Sex'] for p in passengers if int(p['Survived']) == 0]

#Piechart
from collections import Counter
plt.title('Survived')
plt.pie(Counter(survived).values(), labels = Counter(survived).keys(), autopct='%1.1f%%', colors = ('lightblue', 'lightgreen'))
plt.show()

#Gender distribution by survival
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.bar(Counter(gender_survived).keys(), Counter(gender_survived).values(), color = ['blue', 'lightblue'])
ax1.set_title('Survived')
ax1.set_xlabel('Gender')
ax1.set_ylabel('Number')
ax2.bar(Counter(gender_died).keys(), Counter(gender_died).values(), color = ['green', 'lightgreen'])
ax2.set_title('Died')
ax2.set_xlabel('Gender')
ax2.set_ylabel('Number')
fig.suptitle('Gender Distribution by Survival')