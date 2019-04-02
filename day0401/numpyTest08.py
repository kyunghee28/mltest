import numpy as np

a = [1,3,5,7,9]
b = [2,4,6,8,10]

c = a+b
print(c) # [1, 3, 5, 7, 9, 2, 4, 6, 8, 10] : 두개의 배열을 합쳐준다.

arr1 = np.array(a)
arr2 = np.array(b)
r = arr1+arr2   # 각 요소끼리 연산하는 것 : vector operation
print(r) # [ 3  7 11 15 19]

d = arr1+1  # 배열의 수만큼 연산을 하는 것 : broadcasting
print(d)

k = arr1 ** 2
m = arr1 > 5

print(k) # [ 1  9 25 49 81]
print(m) # [False False False  True  True]


i = [1,3,5,7,9]
l = [0,4,6,8,8]
arr3 = np.array(i)
arr4 = np.array(l)
s = arr3 > arr4
print(s) # [True False False False  True]
