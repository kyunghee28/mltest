import numpy as np

a = np.arange(12).reshape(-1,4)

# a 배열과 동일한 shape의 배열을 생성하고 0으로 채워라.
b = np.zeros_like(a)
c = np.zeros(a.shape, dtype='int32')
print(b)
print(c)


# a = np.zeros([3,4],dtype='int32')
# print(a)

# b = np.arange(12).reshape(-1,4)
# print(b)
# print(np.sum(b)) # 전체 데이터 합을 구해준다.
# print(np.sum(b, axis=0))  # axis=0 : 열의 합
# print(np.sum(b, axis=1))  # axis=1 : 행의 합

# a = np.arange(12).reshape(-1,4)
# print(np.max(a)) # 전체 데이터 중에 최대값
# print(np.max(a,axis=0)) # 열에서 최대값
# print(np.max(a,axis=1)) # 행에서 최대값