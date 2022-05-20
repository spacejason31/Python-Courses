#Openening files
# f = open('pg37431.txt')
# text = f.read()
# print(text)
# text

# with open('pg37431.txt') as f:
#     print(f.read(8))

# with open('pg37431.txt') as f:
#     print(f.readline())

# f = open("log.txt", "w+")
# from datetime import datetime
# import time
# for i in range(0,10):
#     print(datetime.now().strftime('%Y%m%d_%H:%M:%S - '), i)
#     f.write(datetime.now().strftime('%Y%m%d_%H:%M:%S - '))
#     time.sleep(1)
#     f.write(str(i))
#     f.write("\n")
# f.close()

#Working with errors
x = 2
assert x<1, "Invalid Value"

def avg(marks):
    assert len(marks) != 0, "Lenghth of marks can not be 0."
    return round(sum(marks)/len(marks), 2)

sem1_marks = [62, 65, 75]
print("Average marks for semester 1:", avg(sem1_marks))

ranks = []
print("Average marks for semester 1:", avg(ranks))

#Plotting
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Scatterplot
temperature = [14.2, 16.4, 11.9, 12.5, 18.9, 22.1, 19.4, 23.1, 25.4, 18.1, 22.6, 17.2]
sales = [215.20, 325.00, 185.20, 330.20, 418.60, 520.25, 412.20, 614.60, 544.80, 421.40, 445.50, 408.10]
plt.scatter(temperature, sales, color = 'red')
plt.show()
plt.title('Ice-cream sales versus Temperature')
plt.xlabel('Temperature (C)')
plt.ylabel('Sales ($)')
plt.scatter(temperature, sales, color='red')
plt.show()

# Line graph
stock_price = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45, 196.42, 200.32, 200.32, 200.85, 199.2, 199.2, 199.2, 199.46, 201.46, 197.54, 201.12, 203.12, 203.12, 203.12, 202.83, 202.83, 203.36, 206.83, 204.9, 204.9, 204.9, 204.4, 204.06]
t = list(range(1, 31))
plt.plot(t, stock_price, marker = '.')
plt.title('Opening Stock Prices')
plt.xlabel('Days')
plt.ylabel('$ USD')
plt.xticks([1, 8, 15, 22, 28])
plt.show()

# Bar chart / horizontal bar chart
grades = ['A', 'B', 'C', 'D', 'E', 'F']
students_count = [20, 30, 10, 5, 8, 2]
plt.bar(grades, students_count, color = ['green', 'blue', 'gray', 'gray', 'gray', 'red'])
plt.barh(grades, students_count, color = ['green', 'blue', 'gray', 'gray', 'gray', 'red'])

# Heatmap
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def heatmap(data, row_labels, col_labels, ax=None, cbar_kw={}, cbarlabel="", **kwargs):
    if not ax:
        ax = plt.gca()
    im = ax.imshow(data, **kwargs)

    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va='bottom')

    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    plt.setp(ax.get_xticklabels(), rotation=-30, ha='right', rotation_mode='anchor')

    for edge, spine, in ax.spines.items():
        spine.set_visible(False)
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar

data = np.array([
    [30, 20, 10,],
    [10, 40, 15],
    [12, 10, 20]
])

im, cbar = heatmap(data, ['Class-1', 'Class-2', 'Class-3'], ['A', 'B', 'C'], cmap='YlGn', cbarlabel='Number of Students')

def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                    textcolors=["black", "white"],
                    threshold=None, **textkw):
    import matplotlib
    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

im, cbar = heatmap(data, ['Class-1', 'Class-2', 'Class-3'], ['A', 'B', 'C'], cmap='YlGn', cbarlabel='Number of Students')
texts = annotate_heatmap(im, valfmt="{x}")

# Density plot in seaborn
import seaborn as sns
data = [90, 80, 50, 42, 89, 78, 34, 70, 67, 73, 74, 80, 60, 90, 90]
sns.distplot(data)

plt.title('Density Plot')
plt.xlabel('Score')
plt.ylabel('Density')
sns.distplot(data)
plt.show()

#Contour plot in seaborn
import seaborn as sns
import matplotlib.pylab as plt
weight=[85.08,79.25,85.38,82.64,80.51,77.48,79.25,78.75,77.21,73.11,82.03,82.54,74.62,79.82,79.78,77.94,83.43,73.71,80.23,78.27,78.25,80.00,76.21,86.65,78.22,78.51,79.60,83.88,77.68,78.92,79.06,85.30,82.41,79.70,80.16,81.11,79.58,77.42,75.82,74.09,78.31,83.17,75.20,76.14]
sns.kdeplot(list(range(1, 45)), weight, kinde='kde', cmap='Blues')

plt.legend(labels=['a', 'b'])
plt.title('Weight Dataset - Contour Plot')
plt.ylabel('height (cm)')
plt.xlabel('width (cm)')
sns.kdeplot(list(range(1,45)),weight, kind='kde', cmap="Blues")

#Multiple graphs
import matplotlib.pyplot as plt
# Split the figure into 2 subplots
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121) # 121 means split into 1 row , 2 columns, and put in 1st part.
ax2 = fig.add_subplot(122) # 122 means split into 1 row , 2 columns, and put in 2nd part.
#Pie Chart (Subplot 1)
labels = ['Adrian', 'Monica', 'Jared']
num = [230, 100, 98]
ax1.pie(num, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'yellow'])
ax1.set_title('Pie Chart (Subplot 1)')
# Plot Bar Chart (Subplot 2)
labels = ['Adrian', 'Monica', 'Jared']
num = [230, 100, 98]
plt.bar(labels, num, color=['lightblue', 'lightgreen', 'yellow'])
ax2.set_title('Bar Chart (Subplot 2)')
ax2.set_xlabel('Candidate')
ax2.set_ylabel('Votes')
fig.suptitle('Voting Results', size=14)

#3D Plots
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
X = np.linspace(0, 10, 50)
Y = np.linspace(0, 10, 50)
X, Y = np.meshgrid(X, Y)
Z = (np.sin(X))
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

