import random
from Data_Science_Apps.animals import Herbivore, Island, HarshIsland
import matplotlib.pylab as plt

A = Herbivore(10)
A.age
A._age()
A.age
A.survival_skill
random.seed(123)
A2 = A.breed()
A2.survival_skill

I = Island(initial_pop=10, max_pop = 100)
I.year
I.animals
stats = I.compute_epochs(15)
stats

#Simulate general & harsh islands
params = {'initial_pop': 10, 'max_pop': 100}
years, N_Islands = 15, 1000

islands = [Island(**params) for _ in range(N_Islands)]
stats = [island.compute_epochs(years) for island in islands]
# stats
params = {'initial_pop': 10, 'max_pop': 100, 'env_range':[20,80]}
years, n_islands = 15, 1000

h_islands = [HarshIsland(**params) for _ in range(n_islands)]
h_stats = [island.compute_epochs(years) for island in h_islands]

# Generate plots for the 2 simulations
plt.style.use('fivethirtyeight')

data = {'Heaven Islands':stats, 'Harsh Islands': h_stats}
colors = {'Heaven Islands': 'blue', 'Harsh Islands': 'red'}

fig, axes = plt.subplots(4, 2, figsize=(10,10), sharex=True)

for i, title in enumerate(('Population', 'Average age', 'Average Survival Skill', '% with SSK > 75')):
    axes[i][0].set_ylabel(title)

    axes[i][0].set_xlim(0, 15)
    axes[i][1].set_xlim(0, 15)

for i, (k, v) in enumerate(data.items()):
    axes[0][i].set_title(k, fontsize=10)

    for s in v: # for each island
        years = list(s.keys())

        axes[0][i].plot(years, [v['pop'] for v in s.values()],
                                  c=colors[k], label=k, alpha=.007)
        axes[1][i].plot(years, [v.get('mean_age', None)
            for v in s.values()], c=colors[k], label=k, alpha=.007)
        axes[2][i].plot(years, [v.get('mean_skill', None)
            for v in s.values()], c=colors[k], label=k, alpha=.007)
        axes[3][i].plot(years, [v.get('75_skill', None)
            for v in s.values()], c=colors[k], label=k, alpha=.007)