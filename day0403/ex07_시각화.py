import matplotlib.pyplot as plt
import numpy as np


#예제 1.
# qty = np.array([60,100,30,40,150])
# plt.plot(qty)
# plt.show()

#                 월   화   수  목   금    월 화  수 목 금   월 화 수 목 금
qty2 = np.array([[1000,1100,1000,900,1500],[80,80,100,50,40],[60,70,40,50,60]]) # 1행 포도, 2행 수박, 3행 딸기

# 예제 2. 수박에 대한 판매량의 정보를 차트로 나타내 봅시다.
# plt.plot(qty2[1])
# plt.plot(qty2[1],'ro')
# plt.show()

# 예제 3. 수박의 평균판매량을 계산하여 평균판매량과의 차이
# 방법1.
# avg = np.average(qty2[1])  # 수박의 평균판매량 -> 70.0
# plt.plot(np.abs(qty2[1]-avg),'ro')

# 방법2.
# plt.plot(np.abs(qty2[1]- np.mean(qty2[1])),'ro')
# plt.show()

# 예제 3-2. x축에는 판매량, y축에는 평균판매량과의 차이
# plt.plot(qty2[1],np.abs(qty2[1]- np.mean(qty2[1])),'bo')
# plt.show()

# 예제 4-1.
# height = np.array([170,180,160,185,167])
# weight = np.array([80,100,65,105,73])
#
# plt.plot(height,weight,'bo')
# plt.xlim(150,200)
# plt.ylim(50,120)
# plt.show()

# 예제 5. x 범위가 -10에서 10 일때 x 의 제곱값을 차트로 그려주세요
# x = np.arange(-10,11,1)
# y = x ** 2
# plt.plot(x,y)
# plt.plot(x,y,"rx")
# plt.show()

# 예제 6.
num = np.arange(0,5,0.1)
num2 = np.arange(0,5,0.02)

# figure 새로운 도화지를 만들어 달라는 것
# plt.figure(1)
# plt.plot(num,"ro")
#
# plt.figure(2)
# plt.plot(num2,"bo")

# 하나의 도화지 안에서 2개의 그래프 그려주는 것 => subplot
# plt.subplot(211)    # 2행 1열에 1번째
# plt.plot(num,'ro')
# plt.subplot(212)    # 2행 1열에 2번째
# plt.plot(num2,'bo')
# plt.show()

# 예제 7.
print(np.exp(2)) # 지수함수
print(np.log(2)) # 로그함수

#  0.01에서 0.01씩 증가하여 2까지의 수들에 대한 지수 값과 로그값을 하나의 화면에 차트를 그려보세요
# a = np.arange(0.01,2,0.01)
# log = np.log(a) # 로그값
# n = np.exp(a) # 지수값
#
# plt.subplot(121)
# plt.plot(n,'r')
#
# plt.subplot(122)
# plt.plot(log,'b')
#
# plt.show()

# 예제 8. 막대그래프

import matplotlib.font_manager as fm
path= 'C:/WINDOWS/Fonts/H2GPRM.TTF' # 글꼴이 있는 위치
fontprop=fm.FontProperties(fname=path, size=18)

qty = [10,20,10,30,50]
plt.bar(range(5), qty, 0.4)  # 0.4는 막대그래프 굵기
plt.title("요일별 과일판매량",fontproperties=fontprop)

plt.show()






