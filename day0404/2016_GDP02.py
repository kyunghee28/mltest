import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager,rc,colors
import csv

f = open('Data/2016_GDP.txt','r',encoding="UTF-8") # r : 읽기용도
f.readline() # 순위:국가:미 달러($) ->  파일의 첫 번째 줄을 읽어 출력

name , money = [] ,[]  # 나라이름과 GDP를 추출

# csv에 reader 함수를 이용해 데이터 읽어오기
# 파일(2016_GDP.txt)에 1:룩셈부르크:101,715 이런식으로 데이터가 들어있음.
list = csv.reader(f, delimiter=":") # delimiter=":" => 구분자가 :(콜론)으로 되어 있어.
# print(list) # <_csv.reader object at 0x00000000139259A0>

for row in list:
    #print(row) # 결과 : ['1', '룩셈부르크', '101,715']
    name.append(row[1])
    money.append(int(row[2].replace(",","")))

f.close()

# 한글 글꼴 설정 - 차트 그리기전
rc('font',family=font_manager.FontProperties(fname="C:/WINDOWS/Fonts/H2GPRM.TTF").get_name())

plt.bar(name[:10],money[:10],color="g")
plt.xticks(name[:10],name[:10], rotation="90") # rotation="90" : x축에 국가 이름들이 세로로 출력된다.

plt.ylabel("GDP")
plt.title("2016년 GDP TOP10")
plt.show()

