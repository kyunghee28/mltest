import numpy as np
import pandas as pd
import xlrd

df = pd.read_excel('../world-series/MLB World Series Champions_ 1903-2016.xlsx')
# print(df.head())
'''
   Year           Champion  Wins  Losses  Ties  WinRatio
0  1903   Boston Americans    91      47     3     0.656
1  1905    New York Giants   105      48     2     0.684
2  1906  Chicago White Sox    93      58     3     0.614
3  1907       Chicago Cubs   107      45     3     0.700
4  1908       Chicago Cubs    99      55     4     0.639
'''
# print(df.columns)   # Index(['Year', 'Champion', 'Wins', 'Losses', 'Ties', 'WinRatio'], dtype='object')

# 예제1. 팀별로 챔피언된 횟수를 출력
Champion_cnt = df.pivot_table(values='Wins', index='Champion', aggfunc='count')
# print(Champion_cnt)

# 예제2. 팀별로 평균승률을 출력하세요
team_WinRatio = df.pivot_table(values='WinRatio', index='Champion', aggfunc='mean')
# print(team_WinRatio)

# 예제3. 평균승률이 높은 상위 5개의 팀을 출력합니다.
team_WinRatio = team_WinRatio.sort_values(by='WinRatio', ascending=False)
# print(team_WinRatio[:5])

# 예제 4.  2000년 이후 데이터 중에 평균승률이 높은 상위 5개 팀을 출력
# top_5 = df['Year'] >= 2000
# print(top_5)    # Fasle, True 로 반환

year_2000 = df[df['Year'] >= 2000]
# print(year_2000)
'''
    Year               Champion  Wins  Losses  Ties  WinRatio
95   2000       New York Yankees    87      74     0     0.540
96   2001   Arizona Diamondbacks    92      70     0     0.568
97   2002         Anaheim Angels    99      63     0     0.611
98   2003        Florida Marlins    91      71     0     0.562
99   2004         Boston Red Sox    98      64     0     0.605
    ...  2000년 이후 데이터만 가져옴
'''

year_2000 = year_2000.pivot_table(values='WinRatio', index='Champion', aggfunc='mean')

year_2000 = year_2000.sort_values(by='WinRatio', ascending=False)
# print(year_2000.head(5))

# 예제 5. 우승한 횟수가 100승이상인 팀을 출력해 주세요
df = pd.read_excel('../world-series/MLB World Series Champions_ 1903-2016.xlsx')
wins_100 = df[df['Wins'] >= 100]
# print(wins_100['Champion'].unique())    # .unique() => 중복이 안되게 출력해 주세요
# print(len(wins_100['Champion'].unique()))

# 예제 6. New York Yankees 팀이 처음 우승한 연도와 마지막으로 우승한 연도를 출력

NY = df[df['Champion'] == 'New York Yankees']
# print(NY)

# 방법1.
NY_Wins = NY.sort_values(by='Year')
firstWins , lastWins = NY_Wins.iloc[0]['Year'], NY_Wins.iloc[-1]['Year']
# firstWins , lastWins = NY_Wins.tail[0]['Year'], NY_Wins.tail[-1]['Year']
# print("처음 우승한 연도 : ",firstWins)
# print("마지막으로 우승한 연도 : ",lastWins)

# 방법2.
firstYser , lastYser = NY_Wins['Year'].min(), NY_Wins['Year'].max()
# print("처음 우승한 연도 : ",firstYser)
# print("마지막으로 우승한 연도 : ",lastYser)

# 예제 7. 월드시리즈가 열리지 않는 연도를 출력해 봅시다.
df = pd.read_excel('../world-series/MLB World Series Champions_ 1903-2016.xlsx')

# not_Yaer = []
# all_Year = np.arange(1903,2017)
# g_Year = df['Year']
# print(len(all_Year))    # 114
# print(len(g_Year))      # 112

# i = 0
# for y in all_Year:
#     yy = g_Year[i]
#     if y != yy:
#         not_Yaer.append(y)
#         continue
#     i = i + 1
# print(not_Yaer)

# not_Yaer = []
# g_Year = df['Year']
# for i in range(len(g_Year)-1):
#     if g_Year[i+1] -g_Year[i] > 1:
#         not_Yaer.append(g_Year[i]+1)
# print(not_Yaer)


df = pd.read_excel('../world-series/MLB World Series Champions_ 1903-2016.xlsx')
all_Year = np.arange(1903,2017)
g_Year = df['Year']
# print(type(all_Year))   # <class 'numpy.ndarray'>
# print(type(g_Year))     # <class 'pandas.core.series.Series'>


all_Year = np.arange(1903,2017)
g_Year = np.array(df['Year'])

# print(type(all_Year))   # <class 'numpy.ndarray'>
# print(type(g_Year))     # <class 'numpy.ndarray'>

not_Yaer = np.setdiff1d(all_Year,g_Year)    # 범위가 큰것을 먼저 써야 한다.
# not_Yaer = np.setdiff1d(g_Year,all_Year)   # 결과 : []  => 범위가 작은 것을 먼저 기재했으므로
# print(not_Yaer) # [1904 1994]

# 예제 8. 최대 우승팀 top5 팀을 출력
df = pd.read_excel('../world-series/MLB World Series Champions_ 1903-2016.xlsx')
many_wins = df.pivot_table(values='Wins', index='Champion', aggfunc='count')
sorted_many_wins = many_wins.sort_values(by='Wins', ascending=False)
print(sorted_many_wins)
''' 공동 4위가 3팀 공동5위가 3팀이 있음
                        Wins
Champion                    
New York Yankees          27
St. Louis Cardinals       11
Boston Red Sox             7
Los Angeles Dodgers        5
Cincinatti Reds            5
New York Giants            5
Philadelphia Athletics     5
Detroit Tigers             4
Oakland Athletics          4
Pittsburgh Pirates         4
'''
