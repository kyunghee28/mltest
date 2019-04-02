import numpy as np

# 1차원 배열을 0 or 1이외의 다른 값으로 채워라.
a = np.zeros(10)
a2 = np.zeros(10, dtype=np.int32)
b = np.ones(10)
b2 = np.ones(10, dtype=np.int32)
c = np.full(10,5)

print(a)
print(a2)
print(b)
print(b2)
print(c)

# 2차원 배열을 0 or 1이외의 다른 값으로 채워라.
a = np.zeros([3,4], dtype=np.int32)
b = np.ones([3,4], dtype=np.int32)
c = np.full([3,4],9)

print(a)
print(b)
print(c)

# 누적합
a = np.arange(12).reshape(-1,4)
print(np.cumsum(a))
print(np.cumsum(a, axis=0)) # 열의 누적합
print(np.cumsum(a, axis=1)) # 행의 누적합

# a 와 똑같은 구조로
a = np.arange(12).reshape(-1,4)
b = np.zeros_like(a) # a와 똑같은 구조의 0으로 채워진 배열로 만들어줘.
print(b)

c = np.ones_like(a) # a와 똑같은 구조의 1으로 채워진 배열로 만들어줘.
print(c)

d = np.full_like(a,8) # a와 똑같은 구조의 특정값으로 채워진 배열로 만들어줘.
print(d)


a = np.arange(12).reshape(-1,4)
print(a)
print(a[0]) # [0 1 2 3] : 0번째 행 모두
print(a[1:]) # [[ 4  5  6  7][ 8  9 10 11]] : 1행부터 끝까지
print('-'*20)

print(a[0][0]) # 0 : 첫번째 행의 첫번째 열
print(a[-1][-1]) # 11 : 마지막 행의 마지막 열
print(a[1][2]) #  6 : 1번째 행 2번쨰 열의 값 - [행][열]

print('-'*20)
print(a[1:2])  # [[4 5 6 7]] : 1행부터 2-1행까지 - [행]
print(a[0:2]) # [[0 1 2 3][4 5 6 7]] : 0행부터 2-0행까지

print('-'*20)
print(a[:]) # 전부다
print(a[:,1]) # [1 5 9] : 모든행에서 1열

print('-'*20)
print(a[::]) # 전부다
print(a[::-1]) # [[ 8  9 10 11][ 4  5  6  7][ 0  1  2  3]] : 거꾸로 출력
print('-'*20)

# 행,열 모두 거꾸로 출력
print(a[::-1,::-1])


# 테두리가 1로 채워지고 속을 0으로 채워지는 5*5배열을 만들어 봅니다.
a = np.ones([5,5],dtype=np.int32)
a[1:4,1:4] = 0
print(a)

# 행과 열을 바꿔서 출력
a = np.arange(12).reshape(-1,4)
print("a : ",a)

print('*'*20)
# 방법1.
print(a[:,0])
print(a[:,1])
print(a[:,2])
print(a[:,3])

print('*'*20)
#방법2.
# for문을 이용해 행과 열을 바꿔서 출력
for i in range(4):  # 열의 수만큼 루프돌기
    #rint(i) # i가 0이면 0번쨰 해당하는 열을 다 찍도록
    print(a[:,i]) # 모든행 i 번쨰 열

b = a.transpose()  # transpose : 행,열을 바꿔 새로운 배열을 생성
print(b)