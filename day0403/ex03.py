import numpy as np

# 예제 16. 1차원 배열에서의 데이터 추출
a = [0,1,2,3,4,5,6,7,8,9] # 파이썬 배열
print(a[0])
print(a[1])
print(a[0:3])
print(a[-1])   # 맨 끝에꺼 뽑아와줘.  => 결과 : 9
print(a[-2])   # 결과 : 8
print(a[:])    # 모두 ->  결과 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[3:])   # 결과 : [3, 4, 5, 6, 7, 8, 9]
print(a[:3])   # 결과 : [0, 1, 2] => 끝나는 인덱스는 포함되지 않음!, 시작하는 인덱스는 포함된다.
#print(a[[0,3,5]])
        # 결과 : TypeError: list indices must be integers or slices, not list
                # => 파이썬 배열에는 index Array는 적용되지 않는다.
# print(a[[False,True,False,True,False,False,False,False,False,False]])
        # 결과 :  TypeError: list indices must be integers or slices, not list
                # => boolean Array는 파이썬 배열에 적용되지 않는다.
print(a[0:10:2])   # 결과 : [0, 2, 4, 6, 8]
print(a[::2])   # 결과 : [0, 2, 4, 6, 8]
print(a[::-2])  # 모두 출력하되 거꾸로 => 결과 : [9, 7, 5, 3, 1]


print("*"*20)
b = np.array(a) # numpy 배열
print(b[0])
print(b[0:3])
print(b[-1])
print(b[-2])
print(b[[0,3,5]])   # 결과 : [0 3 5]  => index Array
print(b[[False,True,False,True,False,False,False,False,False,False]])   # 결과 : [1 3]  => boolean Array
print(b[0:10:2])   # 결과 : [0, 2, 4, 6, 8]
print(b[::2])   # 결과 : [0, 2, 4, 6, 8]
print(b[::-1])   # 결과 : [9 8 7 6 5 4 3 2 1 0]

print("*"*20)

# 예제 17. 2차원 배열에서의 slicing
a = [[1,2,3,4,5,6],
     [7,8,9,10,11,12],
     [13,14,15,16,17,18],
     [19,20,21,22,23,24]]
b = np.array(a)
c = np.array([1,2,3,4,5,6,7,8,9])

# 1번째 행에 2번째 열
print(a[1][2])  # 결과 : 9
print(b[1][2])  # 결과 : 9
print('-'*20)

print(c[1]) # 결과 : 2
print(a[1]) # 1번째 행이 출력 -> 결과 : [7, 8, 9, 10, 11, 12]
print(b[1]) # 1번째 행이 출력 -> 결과 : [ 7  8  9 10 11 12]
print('-'*20)

print(c[1:4])  # 결과 : [2 3 4]
print(a[1:4]) # 1번째 행부터 3번째행이 출력
                # -> 결과 : [[7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
print(b[1:4])   # -> 결과 :[[ 7  8  9 10 11 12]
                             # [13 14 15 16 17 18]
                             # [19 20 21 22 23 24]]
print('-'*20)

print(c[:4])  # 결과 : [1 2 3 4]
print(a[:4])  # 결과 : [[7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
print(b[:4]) # -> 결과 :[[ 7  8  9 10 11 12]
                        # [13 14 15 16 17 18]
                        # [19 20 21 22 23 24]]
print('-'*20)

#모두 출력
print(c[:])
print(a[:])
print(b[:])
print('-'*20)

print(a[1:3][:]) # 1행,2행 모든열이 출력 -> 결과 : [[7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
# 데이터 하나를 뽑아 올때는 print(a[1][2]) 와 같은 표현이 가능!
# 범위를 주어서 slicing 을 할 땐 print(a[1:3][1:3]) 이렇게 표현 할 수 없다.
#  ==> fancy indexing 을 사용해야 한다. (형식: 행과 열 컴마(,)로 구분)
#  => 배열명[행 , 열] /  배열명[[index array] , [index array]]   /  배열명[[boolean array] , [boolean array]]
#  ==> 파이썬 array는 사용 불가!

#print(a[1,2])  # 결과 : TypeError: list indices must be integers or slices, not tuple
                    # -> 파이썬 array는 fancy indexing 사용 불가.
print(b[1 , 2]) # 결과 : 9
print('-'*20)

print(b)
print('-'*20)
print(b[1,])  # 결과 : [ 7  8  9 10 11 12]
print(b[1:3 , ])    # 결과 : [[ 7  8  9 10 11 12][13 14 15 16 17 18]]
print(b[[1,2], ]) # 행이 들어가는 자리에 index array 를 사용 => 결과 : [[ 7  8  9 10 11 12][13 14 15 16 17 18]]
print('-'*20)

# 예제 17-2. 모든 행에 대하여 1열부터 4열까지 데이터를 출력
print(b[:,1:5]) # 결과 : [[ 2  3  4  5]
                         # [ 8  9 10 11]
                         # [14 15 16 17]
                         # [20 21 22 23]]
print('-'*20)

# 예제 17-3. 모든 행에 대하여 1,3,5열 데이터를 출력
print(b[:,[1,3,5]]) # 결과 : [[ 2  4  6]
                             # [ 8 10 12]
                             # [14 16 18]
                             # [20 22 24]]
print('-'*20)

# 예제 17-4. 짝수행만 모두 출력
print(b[::2])   # 처음부터 끝까지 2씩 증가하면서 => 결과 : [[ 1  2  3  4  5  6][13 14 15 16 17 18]]
print('-'*20)

# 예제 17-4. 짝수행에 대하여 1열부터 4열까지 출력
print(b[::2,1:5])   # 결과 :[[ 2  3  4  5][14 15 16 17]]
print('-'*20)

# 예제 17-5. 배열중에 9, 12, 14, 17, 20, 22, 23이 있는 요소의
# array indexing을 만들고 fancy indexing 사용해 뽑아오세요













