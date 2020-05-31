import numpy as np

w = np.array([[0.6, 0.1, 0.1, 0.1, 0.1], [0.1, 0.6, 0.1, 0.1, 0.1], [0.1, 0.1, 0.6, 0.1, 0.1], [0.1, 0.1, 0.1, 0.6, 0.1], [0.1, 0.1, 0.1, 0.1, 0.6]])
u = np.array([0.6, 0.5, 0.6, 0.2, 0.1])
h = w.dot(u)
print(h)
M = np.array([[-0.125, 0, 0.125, 0.125, 0], [0, -0.125, 0, 0.125, 0.125], [0.125, 0, -0.125, 0, 0.125], [0.125, 0.125, 0, -0.125, 0], [0, 0.125, 0.125, 0, -0.125]])
val, vec = np.linalg.eig(M)
print(val)
print(vec)
vss = sum([h.dot(vec[x])/(1 - val[x])*vec[x] for x in range(0,4)])
first = h.dot(vec[0])/(1 - val[0])*vec[0]
print(sum(first))
print(vss)