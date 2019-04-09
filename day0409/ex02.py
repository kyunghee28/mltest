# 예제. data1,data2 배열을 만들고
# 		data1 에는 난수 100개를 발생시켜 담도록 합니다. (단, 난수의 범위는 -1,0,1)
# 		data2 에는 data1 요소를 누적한 합이 담기도록 합니다.
# data1,data2를 각각 하나의 figure에 위아래로 분할하여 plot으로 나타내 봅니다.

import  numpy as np
import matplotlib.pyplot as plt
import random

# 방법 1.
# data1 = []
# data1 = np.random.randint(-1,2,100)
# print(data1)
# plt.subplot(211)
# plt.plot(data1)
#
# data2 = []
# y = 0
# for i in data1:
#     y = y + i
#     data2.append(y)
# print(data2)
#
# plt.subplot(212)
# plt.plot(data2)
# plt.show()

# 방법2.
# data1 = []
# data2 = []
# temp = 0
# for _ in range(100):
#     a = np.random.randint(3)-1  # -1 ,0 ,1
#     temp = temp + a
#     data1.append(a)
#     data2.append(temp)
#
# plt.subplot(211)
# plt.plot(data1)
# plt.subplot(212)
# plt.plot(data2)
# plt.show()

# 방법3.
# data1 = np.random.randint(-1,2,100)
# data2 = np.cumsum(data1)    # cumsum => 누적해서 더해준다.
# print(data1)
# print(data2)
# plt.subplot(211)
# plt.plot(data1)
# plt.subplot(212)
# plt.plot(data2)
# plt.show()

# print(plt.style.available)
# ['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
#  'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark',
#  'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper',
#  'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white',
#  'seaborn-whitegrid', 'seaborn', 'Solarize_Light2', 'tableau-colorblind10', '_classic_test']

# 위의 예제를 ggplot 스타일을 적용시켜 차트를 그려봅시다.
# data1 = np.random.randint(-1,2,100)
# data2 = np.cumsum(data1)
# with plt.style.context('_classic_test'):
#     plt.subplot(211)
#     plt.plot(data1)
#     plt.subplot(212)
#     plt.plot(data2)
#     plt.show()

#  data2의 내용을 한화면에 _classic_test를 제외한 25개의 스타일별로 나타내도록 합니다.
data1 = np.random.randint(-1,2,100)
data2 = np.cumsum(data1)
x = plt.style.available
for i in x:
    with plt.style.context(i):
        plt.subplot(len(i),1,len(i))
        plt.plot(data2)
        plt.show()
#