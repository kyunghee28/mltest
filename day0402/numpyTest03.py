import numpy as np
# 다른 자료형으로 배열을 생성
# 정수형의 파이썬배열 -> 실수형의 numpy 배열 생성
# np.array(파이썬 배열, dtype='새로운 자료형')
# 원래 파이썬 배열이 새로운 자료형으로 변환이 가능해햐 한다.

a = [0,1,2,3,4,5]

b = np.array(a, dtype='float64') # 정수형의 데이터를 실수형의 numpy배열로
print(b)

c = np.array(a, dtype='<U1')
print(c)

# d = [0,1,2,3,4,'안녕']
# e = np.array(d, dtype='float64')
# print(e) # 오류 -> 불가능!!!

f = [0,1,2,3,4,'5']
g = np.array(f, dtype='float64')
print(f) # 가능.

