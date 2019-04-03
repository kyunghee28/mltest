import numpy as np

# 예제 18. 속은 0으로 채워지고 테두리는 1로 채워지는 5*5 배열을 만들어 보세요
a = np.array([5,5], dtype='int32')

# 방법1. onse 함수 이용
arr = np.ones(a)
arr[1:4,1:4] = 0
# arr[1:-1,1:-1] = 0
print(arr)

# 방법2. zeros 함수 이용
arr2 = np.zeros(a)
arr2[[0,-1],:] = 1
arr2[:,[0,-1]] = 1
print(arr2)

print("-"*20)
# 예제 19. 0으로 채워진 8*8 배열을 만들고 색이 있는 부분을 1로 만드세요
b = np.zeros([8,8], dtype='int32')

rows = [1,1,2,2,3,3,4,4,5,5,6,6]
cols =[7,6,6,5,5,4,4,3,3,2,2,1]

b[rows,cols] = 1
print(b)

print("-"*20)

# 예제 20. a는 숫자 1일 표현하기 위한 최소한의 정보입니다.
#             a 배열의 요소의 수만큼 행, 요소중에 가장 큰값 +1 만큼 열을 갖는
#             0으로 채워진 2차원 배열을 만들고 각 행의 배열의 요소에 해당하는 열에 1을 설정합니다.

a = [5,5,5,4,3,2]
b = np.zeros([len(a),np.max(a)+1], dtype='int32')

b[range(len(a)),a] = 1
print(b)

# one-hot Encoding
# 기계학습을 시키려면 학습시키고자 하는 정보(내용-글자or그림)를
# 기계학습이 가능할 상태로 만들어야 하는데 one-hot Encoding 기업을 많이 사용한다.

print("-"*20)
# 예제 21.0으로 채워진 5*5 배열을 만들고 대각선으로 1로 채우세요
a = np.zeros([5,5], dtype='int32')
a[[0,1,2,3,4],[0,1,2,3,4]] = 1
print(a)

b = np.eye(5,5, dtype='int32')
print(b)
