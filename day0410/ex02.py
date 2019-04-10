import numpy as np
import pandas as pd
import xlrd

df = pd.read_excel('../world-series/MLB World Series Champions_ 1903-2016.xlsx')
print(df.head())
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
team_WinRatio = team_WinRatio.sort_values(by='WinRatio', ascending='False')[::-1]
print(team_WinRatio[:5])
