import pickle
import matplotlib.pyplot as plt
import numpy as np

with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)

# print(data)
x = data['c10p1'][:, 0]-0.5
y = data['c10p1'][:, 1]+0.5
# print(x)
# print(y)

# update rule w(i+1) = w(i) + dt*nu*(v*u - alpha*v**2*u), v = u*w
nu = 1
alpha = 1
dt = 0.01
np.random.seed(42)
w0 = np.array([-0.5, 0.5])
print(w0)

wnext = w0
for i in range(0, 100000):
    ind = i%100
    v = x[ind]*wnext[0] + y[ind]*wnext[1]
    wnext = wnext + dt*nu*(v*np.array([x[ind], y[ind]]) - alpha*v*v*wnext)
    if i % 10000 == 0:
        print(wnext)

# correlation matrix M = XTX/N
# X = np.dstack((x, y))
# M = X.transpose().dot(X) / 100
# val, vec = np.linalg.eig(M)
# print(val)
# print(vec)
# plt.scatter(x, y)
# plt.show()