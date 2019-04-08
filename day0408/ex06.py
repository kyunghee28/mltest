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
# print(b)
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

# 예제 8. 성별별로 평점 평균의 차이가 가장 많이 나는 영화 5개를 출력해 봅시다.
b['diff'] = (b['F']-b['M']).abs()
# print(b)
'''
    b['diff'] = b['F']-b['M'] 는 음수가 나오닌까 절대값으로!! 
    gender                                                 F         M      diff
    title                                                                       
    $1,000,000 Duck (1971)                          3.375000  2.761905  0.613095
    'Night Mother (1986)                            3.388889  3.352941  0.035948
    'Til There Was You (1997)                       2.675676  2.733333 -0.057658


    ==> 음수가 나오닌까 절대값을 구해야 한다. : abs( ) 함수 사용
        gender                                                     F  ...      diff
    title                                                         ...          
    Last Action Hero (1993)                             2.662338  ...  0.182432
    Postino, Il (The Postman) (1994)                    4.125628  ...  0.052780
    Emma (1996)                                         4.061151  ...  0.406443
    Guns of Navarone, The (1961)                        4.061224  ...  0.107582
'''

c = b.sort_values(by='diff', ascending=False)   # ascending=False : 내림차순
# print(c.head(5))
'''
gender                                         F         M      diff
title                                                               
Dirty Dancing (1987)                    3.790378  2.959596  0.830782
Good, The Bad and The Ugly, The (1966)  3.494949  4.221300  0.726351
Dumb & Dumber (1994)                    2.697987  3.336595  0.638608
Evil Dead II (Dead By Dawn) (1987)      3.297297  3.909283  0.611985
Grease (1978)                           3.975265  3.367041  0.608224
'''


# 예제 9. 남자가 더 좋아하는 영화 5개
a = df.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
b = a.loc[cnt_500.index]
b['M-F'] = b['M']-b['F']
m = b.sort_values(by='M-F', ascending=False)   # ascending=False : 내림차순
print(m.head(5))
'''
gender                                         F         M       M-F
title                                                               
Good, The Bad and The Ugly, The (1966)  3.494949  4.221300  0.726351
Dumb & Dumber (1994)                    2.697987  3.336595  0.638608
Evil Dead II (Dead By Dawn) (1987)      3.297297  3.909283  0.611985
Caddyshack (1980)                       3.396135  3.969737  0.573602
Animal House (1978)                     3.628906  4.167192  0.538286
'''

# 예제 10. 여자가 더 좋아하는 영화 5개
a = df.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
b = a.loc[cnt_500.index]
b['F-M'] =b['F']-b['M']
f = b.sort_values(by='F-M', ascending=False)   # ascending=False : 내림차순
print(f.head(5))
'''
gender                                        F         M       F-M
title                                                              
Dirty Dancing (1987)                   3.790378  2.959596  0.830782
Grease (1978)                          3.975265  3.367041  0.608224
Rocky Horror Picture Show, The (1975)  3.673016  3.160131  0.512885
Mary Poppins (1964)                    4.197740  3.730594  0.467147
Sound of Music, The (1965)             4.233677  3.783418  0.450259
'''


