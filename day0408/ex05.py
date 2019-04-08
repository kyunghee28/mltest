import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pythonTest.day0408.bitutil

df = pythonTest.day0408.bitutil.getMovies()

# 예제. 영화별로 투표건수(별점을 받은 건수)를 출력
title_count = df.pivot_table(values='rating', index='title', aggfunc='count')
# print(title_count)

# 예제. 평가건수가 100개 이상인 영화제목을 출력

# print(title_count['rating']>=100)
'''
title
$1,000,000 Duck (1971)                            False
'Night Mother (1986)                              False
'Til There Was You (1997)                         False
'burbs, The (1989)                                 True
...And Justice for All (1979)                      True
1-900 (1994)                                      False
10 Things I Hate About You (1999)                  True
101 Dalmatians (1961)                              True
101 Dalmatians (1996)                              True
12 Angry Men (1957)                                True

==>  False,True 형식으로 출력
'''
title_500 = title_count[title_count['rating']>=500]

# 평가건수가 500개 이상인 영화제목을 내림차순으로 정렬
title_500_sort = title_500.sort_values(by='rating', ascending='False')
print(title_500_sort)



