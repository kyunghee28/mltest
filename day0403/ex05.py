import numpy as np

# 정렬
# 예제1. 작은순부터 정렬하세요
a = [7,6,9,5,11,2]
arr = np.array(a)
arr.sort()
print(arr)   # 결과 : [ 2  5  6  7  9 11]

# 예제2.
# 정렬했을 때 와야할 데이터 순서를 반환하는 함수 -> argsort
a = [7,6,9,5,11,2]
arr = np.array(a)
idx = np.argsort(arr)
print(idx)   # 결과 : [5 3 1 0 2 4]

print(arr[idx])   # 결과 : [ 2  5  6  7  9 11]
''' 정렬한 순서대로 출력된다.'''

# 예제3-1.
# 판매량이 높은 순으로 과일명을 출력
item = ['사과','오렌지','바나나','망고','복숭아']
qty = [200,85,1000,10,45]

item = np.array(item)
n = np.argsort(qty)[::-1]
print(item[n])   # 결과 : ['바나나' '사과' '오렌지' '복숭아' '망고']

# 예제3-2. 가장 큰 값이 있는 위치 => argmax
n = np.argmax(qty)
print(item[n])   # 결과 : 바나나

# 예제3-3. 최대값이 두개 이상일 때
item2 = ['사과','오렌지','바나나','망고','복숭아','딸기']
qty2 = [200,85,1000,10,45,1000]
# 방법1.
item2 = np.array(item2)
arr_qty = np.array(qty2)

n = np.argwhere(arr_qty == np.amax(arr_qty)) # 최대값이 있는 위치를 알려준다 -> [[2][5]]
print(item2[n].flatten())   # 결과 : ['바나나' '딸기']

# 방법2.
r = item2[n]
r = r.reshape(r.size)
print(r)   # 결과 : ['바나나' '딸기']
























