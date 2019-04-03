import numpy as np

# 예제 10. numpy 배열의 연산
# broadCasting  :   어떤 값 하나가 배열의 요소만큼 연산을 수행
     # ex. 1 + [1,2,3,4,5]
 # vector Operation(vectorization) : 두개의 배열의 인덱스가 같은 요소끼리 연산을 수행
    # ex. [1,2,3] + [4,5,6]       => 열의 크기가 같아야 한다.

# broadCasting
a = np.array([1,2,3,4,5])
b = a + 1
print(b)    #  배열의 요소에 각각 1을 더해 준다. -> broadCasting

print("*"*10)

# vector Operation
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a + b
print(c)

print("*"*10)
# 예제 11. a,b 두 배열을 더하기 해 봅시다. (결과가 2차원 배열이 나오도록)
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[10,20,30],[40,50,60]])
print(a +b)

print("*"*10)
# 예제 12.  a,b가 차원이 다를경우
a = np.array([1,2,3,4,5,6])
b = np.array([[10,20,30],[40,50,60]])

c = a.reshape([2,-1])
print(c+b)

print("*"*10)

# 예제 13.  broadCasting 에 비교연산자를 사용하면 boolean Array 를 얻는다.
a = np.array([1,3,0,7,9,5,6])
b = a > 5
print(b)

print("*"*10)

# 예제 14.  배열의 요소중에 원하는 인덱스의 요소만 추출할 수 있다, => index Array
a = np.array([1,3,0,7,9,5,6])

#  방법 1.
# print(a[0,2,5]) 결과 : 오류 -> IndexError: too many indices for array
            # => a 가 3차원 배열인지 알고 0번째 행의 2번째 열의 5번쨰 면을 찾으려고 함.
print(a[[0,2,5]])  # 결과 : [1 0 5]

idx = [0,2,5]
c = a[idx]
print(c)

#방법 2.
# 0,2,5 번째 요소만 출력하는 것을 boolean Array로 실험해 봅니다.
r = [True,False,True,False,False,True,False]  # -> 추출하고 싶은 인덱스 위치에 True로 주면된다.
print(a[r])

print("*"*10)

# 예제 15.
# 60점 이상이면 합격! 합격한 사람들의 이름을 출력해 봅니다.
name = ['홍길동','유관순','이순신','김유신','강감찬']
score = [80,60,100,40,70]
# 방법1.
n = np.array(name)
s = np.array(score)

s = s >= 60
print(n[s])

# 방법2.
name = np.array(name)
score= np.array(score)
print(n[score >= 60])






