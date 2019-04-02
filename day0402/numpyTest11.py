import numpy as np

a = np.arange(12).reshape(-1,4)
print(a)

print(a > 5)
print(a[a > 5])  # bool Array
print("-"*20)

    # [행,열]
print(a[0,1])   # 0번째 행의 1번째 열
print(a[0])  # 0번째 행
print("-"*20)

# index Array
print(a[[0,1]]) # 0번째 행,1번째 행
print(a[[1,0]]) # 1번째 행,0번째 행

print("-"*20)

    #   행 행 열 열
print(a[[1,0],[0,1]])  # index Array
    # 1행,0행 에서 0열 1열
print("-"*20)

a[[1,0],[0,1]] = 100
print(a)

# 연습 ) index Array를 이용해 테두리가 1로 채워지고 속이 0으로 채워지는 5*5배열
# 전체를 1로 채워서
a = np.ones([5,5], dtype=np.int32)
a[[1,2,3],1:4] = 0
print(a)
print("-"*20)

# 전체를 0으로 채워서
b = np.zeros([5,5], dtype=np.int32)
b[:,[0,-1]] = 1
print(b)
print("-"*20)
b[[0,-1],:] = 1
print(b)

# 연습> 0으로 채워진 5*5배열을 만들어 대각선을 1로 만드세요.( index Array)
a = np.zeros([5,5], dtype=np.int32)
a[[0,1,2,3,4],[0,1,2,3,4]] = 1
print(a)

a = np.zeros([5,5], dtype='int32')
a[range(5),range(5)] = 1
print(a)

a = np.eye(5,5, dtype='int32')
print(a)


# 연습 > a배열의 요소만큼 행의 크기를 갖고 a 배열의 요소중에 최대값 +1 의 열의 크기를 갖는
# 			0으로 채워진 2차원 배열을 만들고 각 행마다 a 배열의 요소에 해당하는 열에 1을 채우시오.

a = [1,3,0,3,1]
b = np.zeros([len(a),np.max(a)+1], dtype='int32')
# 방법1.
for i in range(len(a)):
    b[i,a[i]] = 1
print(b)

print("-"*20)
b[[range(len(a))],a] = 1
print(b)

# 방법2.
a = [1,3,0,3,1]
b = np.eye(len(a),np.max(a)+1,dtype='int32')[a]
print(b)

# 정렬
a = [4,3,1,5,2]
arr1 = np.array(a)

# 정렬을 하면 몇번째 요소부터 순서대로 오는지 배열을 생성
# ex > [2,4,1,0,3] : 1은 배열에서 2번째에 있으닌까 2
b = np.argsort(arr1)
print(b) # 결과 : [2 4 1 0 3]
print(arr1[b]) # 결과 : [1 2 3 4 5]

name = ['유관순','홍길동','강감찬','박주호','이순신','김경희','문재인']
score = [80,90,100,100,70,96,100]
# 성적순 데로 이름 출력
a = np.array(score)
b = np.array(name)

c = np.argsort(a)
print(c)
print(b[c])

d = np.argsort(a)[::-1]
print(d)
print(b[d])

a = [4,3,1,5,2]
arr1 = np.array(a)
r = np.max(arr1)
idx = np.argmax(arr1) # 최대값이 있는 자리의 값을 알려줌.
print(r)
print(idx)

# 연습 > 점수가 가장 높은 학생이 여러명일 경우 이름을 모두 출력
name = ['김경희','유관순','홍길동','강감찬','박주호','이순신','문재인']
score = [100,80,90,100,70,96,100]
# 점수가 가장 높은 학생의 이름을 모두 출력
arr_name = np.array(name)
arr_score = np.array(score)

r = np.argwhere(arr_score == np.amax(arr_score))
#방법1.
r = r.flatten()
print(arr_name[r])
#방법2.
print(r.ravel())
print(arr_name[r].ravel())

# flatten
a = [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]
arr = np.array(a)
arr2 = arr.flatten()
print(arr2) # 차수와 상관없이 무조건 1차원 만들어 준다.


