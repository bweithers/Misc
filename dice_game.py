import random as rd
import seaborn as sns
from numpy import average
import matplotlib.pyplot as plt

def play_round(roll_cutoff):
    score = 0
    while score <= roll_cutoff:
        score += rd.random()
        if score > 1: 
            return 0
    return score

d = {}
results = []
n = 100000
for i in range(100):
    results = []
    for _ in range(n):
        results.append(play_round(i/100))
    d[i] = results

evs = {k: average(d[k]) for k in d}


# print(evs)
x = [k/100 for k in evs.keys()]
y = [float(evs[k]) for k in evs.keys()]
print(max(y))
# print(x)
# print(y)
sp = sns.scatterplot(x = x, y = y)
plt.show()
sp.savefig("out.png")