import numpy as np

# 파이썬 배열을 numpy배열로
a = [1,2,3,4,5,6]

# a를 numpy배열로
c = np.array(a)
print(type(c))

# numpoy배열을 파이썬 배열로
b = np.arange(6)

# b를 python 배열로
d = list(b)
print(type(d))

