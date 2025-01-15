import numpy as np 
from numpy import linalg as la

x = [[1, 2], [3, 4]]
y = [[4, 2], [1, 3]]


res = []
len_x = len(x)
for i in range(len_x):
    l = []
    for j in range(len_x):
        num = 0
        for k in range(len_x):
            num += x[i][k] * y[k][j]
        l.append(num)
    res.append(l)

print(res)
print(np.array(x) @ np.array(y))

x = np.array(x)

print(la.inv(y) @ y)