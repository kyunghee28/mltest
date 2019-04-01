import numpy as np

# a = [1,2,3,4,5,6]
# b = a + 1
# print(b) : 오류

arr = [1,2,3,4,5,6]
a = np.array(arr)
b = a+1   # broadcasting : 배열의 수만큼 연산을 하는 것
print(b) # [2 3 4 5 6 7]
