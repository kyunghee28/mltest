# 난수만들기
# -> random을 이용할 수도 있고 numpy를 이용할 수도 있다.

import  numpy as np
import matplotlib.pyplot as plt
import random

#예제 1 )  0 ~ 10 사이의 난수를 발생
# x = np.random.randint(10)   # 시작값 생략 가능.
# print(x)
# x2 = random.randint(0,10)
# print(x2)

#예제 2 ) 100 ~ 1000사이에 난수 5개를 발생
# x = np.random.randint(100,1000,5)
# print(x)
#
# #예제 2 -2) 100 ~ 1000사이에 난수 1개를 발생
# x2 = np.random.randint(100,1000)
# print(x2)

# 예제 3) 이미 있는 데이터들 중에 임의로 하나를 선택  random => choice
# data = [9,7,2,1,100,3]
# x = random.choice(data)
# print(x)

# 예제 4) 이미 있는 데이터들을 섞어서 중복없이 임의로 여러 개 선택(random => sample)
# data = [9,7,2,1,100,3]
# x2 = random.sample(data,3)
# print(x2)

#  예제 5) 0~100사이에 난수 1개
# x = np.random.randint(100)
# print(x)

# x = np.random.randint(0,1000,100)
# print(x)

x = np.random.rand()    # 0~1사이에 실수 1개를 발생
print(x)

# #  0~1 사이에 실수 100개
# x = np.random.rand(100)
# print(x)
#
# # 비교>  1~100사이에 정수 1개
# x = np.random.randint(100)

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x,y,c='r')
plt.show()
