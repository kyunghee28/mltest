import numpy as np

# 0~5까지의 정수가 들어있는 2행 3열을 만드세요.(3가지)
# 방법1.
a = np.arange(6)
b = a.reshape(2,3)
print(b)

# 방법2.
c = np.array([[0,1,2],[3,4,5]])
print(c)

# 방법3.
d = np.arange(0,6)
e = d.reshape(2,3)
print(e)

# 방법4.
f = [0,1,2,3,4,5]
g = np.array(f).reshape(2,3)
print(g)

# 방법5.
h =[[0,1,2],[3,4,5]]
arr = np.array(h)
print(arr)