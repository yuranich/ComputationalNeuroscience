import numpy as np

Q = np.array([[0.2, 0.1], [0.1, 0.3]])
val, vec = np.linalg.eig(Q)
print(val)
print(vec)

