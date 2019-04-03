import numpy as np

#np.zeros   배열의 요소를 0으로 채워주세요
#np.ones    배열의 요소를 1으로 채워주세요
#np.full    배열의 요소를 특정값을 채워주세요

# 예제 1.
a = np.zeros(10, dtype='int32')
b = np.ones(5, dtype=np.int32)
c = np.full(7,100)

print(a)
print(b)
print(c)

print('*'*20)
# 예제 2. 2 차원 배열을 특정값으로 채워지도록.
a = np.zeros([2,3], dtype=np.int32)
b = np.ones([5,5], dtype=np.int32)
c = np.full([5,5], 100)

print(a)
print(b)
print(c)

print('*'*20)
# 예제 3. 연속된 데이터를 갖는 numpy 배열 생성 : np.arange
a = np.arange(10)
print(a)

b = np.arange(1,11)
print(b)

c = np.arange(1,11,2)
print(c)

d = np.arange(5,-5,-1)
print(d)

print('*'*20)
# 예제 4. 파이썬 배열을 numpy배열로 : np.array
a = [1,2,3,4,5]
b = np.array(a)
print(a) # 결과 : [1, 2, 3, 4, 5] -> 파이썬 배열
print(b) # 결과 : [1 2 3 4 5] -> numpy 배열
# 특정 데이터 뽑아오기
print(a[2]) # 결과 : 3
print(b[2]) # 결과 : 3

print('*'*20)
# 예제 5. numpy배열을 파이썬 배열로 : list
c = np.arange(5,-5,-1)
d = list(c)
print(c) # 결과 : [ 5  4  3  2  1  0 -1 -2 -3 -4] -> numpy 배열
print(d) # 결과 : [5, 4, 3, 2, 1, 0, -1, -2, -3, -4] -> 파이썬 배열
print(type(c)) # 결과 : <class 'numpy.ndarray'>
print(type(d)) # 결과 : <class 'list'>

print('*'*20)
# 예제 6. 배열의 차수 , 모양(몇행 몇열인지) 확인,  요소의 자료형 확인
e = np.array([1,2,3,4,5]) # 정수형의 numpy 배열
f = np.array([10.5,2.7,3.5]) # 실수형의 numpy 배열
g = np.array([[1,2,3],[4,5,6]])
print(e)
print(f)

# 배열의 자료형 -> type : 배열자체가 numpy배열인지 python배열인지
print(type(e))  # 결과 :  <class 'numpy.ndarray'>
print(type(f)) # 결과 :  <class 'numpy.ndarray'>

# 배열 요소의 자료형 -> dtype
print(e.dtype) # 결과 :  int32
print(f.dtype) # 결과 :  float64

# 배열의 차수  ->  ndim
print(e.ndim)   # 결과 : 1 -> 1차원이다.
print(f.ndim)   # 결과 : 1
print(g.ndim)   # 결과 : 2 -> 2차원이다.

#모양(몇행 몇열인지) -> shape
print(e.shape)   # 결과 : (5,) -> 데이터가 5개 있는 1차원 배열
print(f.shape)   # 결과 : (3,)
print(g.shape)   # 결과 : (2, 3) -> 2행 3열이다.

print('*'*20)
# numpy 배열의 차원을 변경 : reshape
a = np.array([1,2,3,4,5,6])
b = a.reshape([2,3]) # `1차원 배열을 2행 3열으로
print(a)
print(b)

print('*'*20)
# 예제 7. 차원을 변경할 때 행이나 열중에 하나를 생략
a = np.array([1,2,3,4,5,6])
b = a.reshape([2,-1]) # 2행으로 해주고 열은 마음데로 해줘.
c = a.reshape([-1,3]) # 3열로 해주고 행은 마음데로 해줘.

print(b)
print(c)

print('*'*20)
# 예제 8. 2차원 배열을 다시 1차원 배열으로
# => 내가 직접 데이터의 수를 파악하기 보다는 shape를 통해 행,열 만큼의 배열을 생성하도록 합니다.
a = np.array([[1,2,3],[4,5,6]])

# 방법1,
print(len(a[0])) # 결과 : 3
print(len(a))   # 결과 : 2
b = a.reshape(len(a) * len(a[0]))
print(b)

# 방법2,
row,col = a.shape
print(row)
print(col)
c = a.reshape(row * col)
print(c)

print('*'*20)

