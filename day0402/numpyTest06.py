import numpy as np

a = np.arange(3)
print(a)
print(a + 1) # a의 각 요소에 +1 : BoardCasting
print(a > 1) # a의 각 요소가 1보다 큰지 비교 :  BoardCasting
print(a[a > 1]) # a > 1 식을 만족하는 데이터만 출력
print(a[a >= 1])

print('-'*50)
# 3개(b,c,d)다 똑같은표현
b = np.arange(6).reshape(2,3)
c = np.arange(6).reshape(2,-1)
d = np.arange(6).reshape(-1,3)

print("b : ",b)
print("c : ",c)
print("d : ",d)
print('d+1 : ',d+1)
print('d>1 : ',d>1)  # d의 요소만큼 비교하여 False,True를 반환 : BoardCasting
print('d[d>1] : ',d[d>1]) # BoardCasting의 True의 요소만 출력
