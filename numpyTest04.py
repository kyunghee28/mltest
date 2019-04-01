import numpy as np

a = np.arange(6)
# 차수를 바꾸는 방법 -> reshape
b = a.reshape(2,3) # 2행 3열로 만들어 주세요

print(a) # [0 1 2 3 4 5]
print(b)
    #[[0 1 2]
    #  [3 4 5]]


# shape : 차원을 확인해줌.
print(a.shape) #(6,)
print(b.shape) #(2, 3)

# 차원을 변경하려면 데이터수가 맞아야한다.
# c = np.arange(7)
# d = c.reshape(2,3)
# print("d",d) # 오류 :  데이터수가 맞지 않아서 오류!

