import matplotlib.pyplot as plt

# 방법1.
# x = []
# y = []
# for i in range(-10,11,1):
#     x.append(i)
#     y.append(i*i)
#
# plt.plot(x,y,"ms--")
# plt.xlim(-10,10)
# plt.ylim(0,100)
# plt.show()

# 방법2.
# for i in range(-10,11,1):
#     plt.plot(i, i*i, "m*")
# plt.xlim(-10,10)
# plt.ylim(0,100)
# plt.show()

# 방법3.
import numpy as np
#
# x = np.arange(-10,10,0.5)
# print(x)
#     # [-10.   -9.5  -9.   -8.5  -8.   -7.5  -7.   -6.5  -6.   -5.5  -5.   -4.5
#     #   -4.   -3.5  -3.   -2.5  -2.   -1.5  -1.   -0.5   0.    0.5   1.    1.5
#     #    2.    2.5   3.    3.5   4.    4.5   5.    5.5   6.    6.5   7.    7.5
#     #    8.    8.5   9.    9.5]
# y = x ** 2
#
# plt.plot(x,y,"r*")
# plt.show()

# -10에서 10까지의 범위안에 균등하게 간격을 두어 100개의 값(데이터)를 생성
x = np.linspace(-10,10,100)
# print(x)
y = np.sin(x)

plt.plot(x,y,"m")
plt.show()
