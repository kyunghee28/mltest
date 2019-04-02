import numpy as np

a = [1,2,3,4,5]
b = [1.0,2.0,3.0,4.0,5.0]
c = ['a','b','c','d','e']
d = ['hello','java','python','oracle','mongo']
e = ['김경희','박민서','이혜민','김종대','김종인']
f = ['a','b','우리나라 대한민국','김경희']

arr1 = np.array(a)
arr2 = np.array(b)
arr3 = np.array(c)
arr4 = np.array(d)
arr5 = np.array(e)
arr6 = np.array(f)

print(arr1.dtype) # int32
print(arr2.dtype) # float64
print(arr3.dtype) # <U1
print(arr4.dtype) # <U6
print(arr5.dtype) # <U3
print(arr6.dtype) # <U9

print(arr1.shape) # (5,) : 1차원이면서 데이터의 수가 5개라는 정보를 확인할 수 있다.
print(arr1.ndim) # 1 : 1차원이라는 정보를 확인할 수 있다.
print(arr1.dtype) # int32 : 요소하나를 위한 자료형이 int32인 것을 알 수 있다.

