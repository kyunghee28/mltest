import numpy as np
import pandas as pd
import pythonTest.day0408.bitutil

df = pythonTest.day0408.bitutil.getMovies() # 전체 영화의 정보
cnt_500 = pythonTest.day0408.bitutil.get_500_Movies() # 500명이상한테 평가받은 영화의 정보

# print(cnt_500.columns)  # Index(['rating'], dtype='object')
# print(cnt_500.index)
'''
Index(['Last Action Hero (1993)', 'Postino, Il (The Postman) (1994)',
       'Emma (1996)', 'Guns of Navarone, The (1961)', 'Body Heat (1981)',
       'Alien Nation (1988)', '28 Days (2000)', 'Peggy Sue Got Married (1986)',
       'Halloween (1978)', 'Ice Storm, The (1997)',
       ...
       'Silence of the Lambs, The (1991)', 'Back to the Future (1985)',
       'Matrix, The (1999)', 'Terminator 2: Judgment Day (1991)',
       'Saving Private Ryan (1998)', 'Jurassic Park (1993)',
       'Star Wars: Episode VI - Return of the Jedi (1983)',
       'Star Wars: Episode V - The Empire Strikes Back (1980)',
       'Star Wars: Episode IV - A New Hope (1977)', 'American Beauty (1999)'],
      dtype='object', name='title', length=618)
'''

# 평가한 사람이 500명이상인 영화중에 성별별,영화별로 별점의 평균을 출력

a = df.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
b = a.loc[cnt_500.index]
print(b)
'''
gender                                                     F         M
title                                                                 
Last Action Hero (1993)                             2.662338  2.479905
Postino, Il (The Postman) (1994)                    4.125628  4.072848
Emma (1996)                                         4.061151  3.654709
Guns of Navarone, The (1961)                        4.061224  3.953642
Body Heat (1981)                                    3.943925  4.055416
Alien Nation (1988)                                 3.433333  3.195946
28 Days (2000)                                      3.209424  2.977707
            ...
Star Wars: Episode VI - Return of the Jedi (1983)   3.865237  4.069058
Star Wars: Episode V - The Empire Strikes Back ...  4.106481  4.344577
Star Wars: Episode IV - A New Hope (1977)           4.302937  4.495307
American Beauty (1999)                              4.238901  4.347301

[618 rows x 2 columns]
'''
