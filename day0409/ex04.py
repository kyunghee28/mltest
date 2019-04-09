import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
from wordcloud import WordCloud


#예제. 문재인 대통령 연설문을 워드 클라우드로 표현해봅시다.
f = open('../data/moon.txt', 'r' ,encoding='UTF-8')
data = f.read()
# print(data)

font = 'C:/Windows/Fonts/DXKPMB-KSCpc-EUC-H.ttf'
speech = WordCloud(font_path = font, background_color='white', width=800, height=600).generate(data)
rc("font",family=font_manager.FontProperties(fname=font).get_name())
plt.imshow(speech)
plt.title("문재인 대통령 연설문")
plt.axis("off")
plt.show()
