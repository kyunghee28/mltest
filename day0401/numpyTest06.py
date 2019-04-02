import numpy as np

# 2차원을 1차원으로 변경
arr = [[1,2,3],[4,5,6]]
a = np.array(arr).reshape(6)
b = list(a)

print(a) # [1 2 3 4 5 6]
print(type(a)) # <class 'numpy.ndarray'>
print(b)  # [1, 2, 3, 4, 5, 6]
print(type(b))  # <class 'list'>

