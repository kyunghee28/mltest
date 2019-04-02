import numpy as np

a = [0,1,2,3,4,5]
arr = np.array(a)
print('arr : ',arr)
print('arr.shape : ',arr.shape)
print("arr.ndim : ",arr.ndim)
print('arr.dtype',arr.dtype)

print("-"*20)

arr2 = arr.reshape(2,3)  # 1차원 배열을 2행 3열로
print('arr2 : ',arr2)
print("arr2.shape :",arr2.shape)
print("arr2.ndim :",arr2.ndim)
print("arr2.dtype",arr2.dtype)


