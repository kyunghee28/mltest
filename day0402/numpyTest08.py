import numpy as np

a = np.arange(3)
b = np.arange(6)
c = np.arange(3).reshape(-1,3)
d = np.arange(6).reshape(-1,3)
e = np.arange(3).reshape(3,-1)

# print('a : ',a) # [0 1 2]
# print('b : ',b) # [0 1 2 3 4 5]
# print('c : ',c) # [[0 1 2]]
# print('d : ',d) # [[0 1 2]
#                    [3 4 5]]
# print('e : ',e) # [[0]
#                    [1]
#                    [2]]

# print('a+b :',a+b) # 오류 : ValueError: operands could not be broadcast together with shapes (3,) (6,)  -> 데이터 수가 다르므로
print('a+c : ',a+c) # 결과 : [[0 2 4]]  a는 1차원 배열 c는 2차원 배열이지만 연산가능!  ->  Vector operation
print('a+d : ',a+d) # 결과 : [[0 2 4][3 5 7]]  a가 d의 1행, 2행과 연산 -> BroadCasting과 Vector operation  수행.
                        # a는 1차원 배열, d는 2차원 배열끼리 연산을 수행하였더니
                        # a 배열이 d배열의 행만큼 연산을 수행 -> BroadCasting
                        # a 배열의 요소 하나하나(0,1,2)가 d 배열의 각 행의 열(0,1,2,3,4,5)과 연산 -> Vector operation
print('a+e : ',a+e) # 결과 : [[0 1 2][1 2 3][2 3 4]] -> Vector operation : e 배열에서 1행이 a배열 1행과 더해 행 하나를 만들고 (Vector operation 1 번), 각 요소마다 연산(Vector operation 2번)

#print('b+c :',b+c)  : 오류 : ValueError: operands could not be broadcast together with shapes (6,) (1,3) -> 데이터 수가 다르므로
# print('b+d :',b+d) : 오류 : ValueError: operands could not be broadcast together with shapes (6,) (2,3)
print('b+e :',b+e)  # e 배열에서 1행이 b배열 1행과 더해 행 하나를 만들고 (Vector operation 1 번), 각 요소마다 연산(Vector operation 2번)-> Vector operation
                        # 결과 : [[0 1 2 3 4 5][1 2 3 4 5 6][2 3 4 5 6 7]]

print('c+d :',c+d) # 결과 : [[0 2 4][3 5 7]]   -> BroadCasting과 Vector operation  수행.
print('c+e :',c+e) # 결과 : [[0 1 2][1 2 3][2 3 4]]  -> BroadCasting

# print('d+e :',d+e) # 오류 : ValueError: operands could not be broadcast together with shapes (2,3) (3,1)