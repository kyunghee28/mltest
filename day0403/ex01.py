import numpy as np

#np.zeros   배열의 요소를 0으로 채워주세요
#np.ones    배열의 요소를 1으로 채워주세요
#np.full    배열의 요소를 특정값을 채워주세요

a = np.zeros(10, dtype='int32')
b = np.ones(5, dtype=np.int32)
c = np.full(7,100)

print(a)
print(b)
print(c)

print('*'*20)
# 2 차원 배열을 특정값으로 채워지도록.
a = np.zeros([2,3], dtype=np.int32)
b = np.ones([5,5], dtype=np.int32)
c = np.full([5,5], 100)

print(a)
print(b)
print(c)

print('*'*20)
# 연속된 데이터를 갖는 numpy 배열 생성 : np.arange
a = np.arange(10)
print(a)

b = np.arange(1,11)
print(b)

c = np.arange(1,11,2)
print(c)

d = np.arange(10,-10,-1)
print(d)