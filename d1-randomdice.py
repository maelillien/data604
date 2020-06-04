import numpy as np
from matplotlib import pyplot as plt

def roll_fair_die():
    return np.random.randint(1,7)

def simulate(ntrials, ndice):
    results=[]
    for i in range(0,ntrials):
        for d in range(0,ndice):
            results.append(roll_fair_die())
    return results


results = simulate(10000,1)

print(np.bincount(results)[1:7])

plt.hist(results, range=(0, max(results)+1), bins=np.arange(1,8,1), align='left', rwidth=0.9)
plt.title('Fair Dice Roll Freqency')
plt.ylabel('Frequency')
plt.xlabel('Roll')
plt.show()

