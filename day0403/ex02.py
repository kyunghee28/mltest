import numpy as np

# numpy 배열의 연산
# broadCasting  :   어떤 값 하나가 배열의 요소만큼 연산을 수행
     # ex. 1 + [1,2,3,4,5]
 # vector Operation(vectorization) : 두개의 배열의 인덱스가 같은 요소끼리 연산을 수행
    # ex. [1,2,3] + [4,5,6]       => 열의 크기가 같아야 한다.

# broadCasting
a = np.array([1,2,3,4,5])
b = a + 1
print(b)    #  배열의 요소에 각각 1을 더해 준다. -> broadCasting

# vector Operation
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a + b
print(c)

# a,b 두 배열을 더하기 해 봅시다. (결과가 2차원 배열이 나오도록)
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[10,20,30],[40,50,60]])
c = a +b
print(c)