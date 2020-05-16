import pickle
from math import atan, degrees

import matplotlib.pyplot as plt

with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

print(data['neuron1'].shape)

stim = data['stim']
mean_rate1 = sum(data['neuron1']) / data['neuron1'].shape[0]
mean_rate2 = sum(data['neuron2']) / data['neuron2'].shape[0]
mean_rate3 = sum(data['neuron3']) / data['neuron3'].shape[0]
mean_rate4 = sum(data['neuron4']) / data['neuron4'].shape[0]

plt.plot(stim, mean_rate1)
plt.plot(stim, mean_rate2)
plt.plot(stim, mean_rate3)
plt.plot(stim, mean_rate4)
plt.xlabel('Stimulus (dir)')
plt.ylabel('Firing rate (Hz)')
plt.title('Tuning curve')

# plt.show()

with open('pop_coding_3.4.pickle', 'rb') as f:
    popcode = pickle.load(f)

print(popcode['c4'])

r1max = max(mean_rate1)
r2max = max(mean_rate2)
r3max = max(mean_rate3)
r4max = max(mean_rate4)

r1 = sum(popcode['r1']) / popcode['r1'].size
r2 = sum(popcode['r2']) / popcode['r2'].size
r3 = sum(popcode['r3']) / popcode['r3'].size
r4 = sum(popcode['r4']) / popcode['r4'].size

v = sum([(r1/r1max) * popcode['c1'], (r2/r2max) * popcode['c2'], (r3/r3max) * popcode['c3'], (r3/r3max) * popcode['c3']])
print(degrees(atan(v[1] / v[0])))