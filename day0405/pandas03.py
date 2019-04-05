import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import matplotlib.pyplot as plt

# 예제) 수학점수가 평균이하인 모든학생의 성적을 막대그래프로 나타내기

df = pd.read_csv('../data/scores.csv')  # csv파일 읽어오기

# 데이터 수가 많을 때는 전체를 파악하기 어렵기 때문에
# 앞이나 뒤에서 몇개만 추출해서 파악할 수 있다.
print(df.head())    # 앞에서 5개만 보여줌
'''
       class    name  kor  eng  mat  bio
    0      1    adam   67   87   90   98
    1      1  andrew   45   45   56   98
    2      1     ben   95   59   96   88
    3      1   clark   65   94   89   98
    4      1     dan   45   65   78   98
'''
print(df.tail())    # 뒤에서 5개만 보여줌
'''
        class    name  kor  eng  mat  bio
    7       2  walter   89   98   78   78
    8       2   oscar  100   78   56   65
    9       2  martin   99   89   87   87
    10      2    hugh   98   45   56   54
    11      2   henry   65   89   87   78
'''

# 칼럼의 수가 너무 많을 때는 head() 5개만 뽑아 왔는데도
# 정신이 없을 수가 있다. 이땐 앞에 데이터 하나만 뽑아와서 데이터의 성격을 파악할 수 있다.
print(df.head(1))
'''
   class  name  kor  eng  mat  bio
0      1  adam   67   87   90   98
'''

print(df.tail(1))
'''
   class  name  kor  eng  mat  bio
11      2  henry   65   89   87   78
'''

# 학생의 이름을 인덱스(키)로 설정
df.index = df['name']

# name 칼럼을 삭제
del df['name']

# 수학점수의 평균을 계산
matavg  = df['mat'].mean()
print(matavg)   #   78.0

# 학생들 중에 수학점수가 평균이하인 학생들의 정보를 추출
lower_math = df[df['mat'] <= matavg]

print(lower_math)
'''
            class  kor  eng  mat  bio
    name                             
    andrew      1   45   45   56   98
    dan         1   45   65   78   98
    paul        2   87   67   65   56
    walter      2   89   98   78   78
    oscar       2  100   78   56   65
    hugh        2   98   45   56   54
'''

rc('font',family=font_manager.FontProperties(fname="C:/WINDOWS/Fonts/H2GPRM.TTF").get_name())

print(plt.colormaps())  # 무슨색이 있는 지 확인
'''
['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']

'''

# 필요한 칼럼만 추출
lower_math[[ 'kor' , 'eng' , 'mat' , 'bio']].plot(kind='bar', colormap='winter')
plt.title("수학점수가 평균이하인 학생")
plt.show()
