# 연습 ) Data폴더의 user.dat, movies.dat, ratings,dat 파일을 읽어들어
# 하나의 DataFrame으로 만들어 봅시다.

#movies.dat
# 영화id::영화제목::장르
# movieid::title::genre
# 1::Toy Story (1995)::Animation|Children's|Comedy

'''
서로 공통이 있는 것으로 합칠 수 있다.
movies.dat 과 rating.dat 은 movieid 가 공통
users.dat 과 rating.dat 은 userid가 공통
'''

import numpy as np
import pandas as pd

# help를 이용하여
# 파일을 읽어 들일때 컬럼헤더는 없다라는 옵션을 설정하고
# 칼럼이름을 읽어들이때 movieId, title, genre 설정하도록 해 봅니다.
# help(pd.read_csv)

# movies = pd.read_csv("../data/movies.dat",sep="::",engine="python")   #상대경로로 접근.
# print(movies)
'''
...은 데이터가 너무 많아서 줄인것임.

29      31  ...                           Drama
...    ...  ...                             ...
3852  3923  ...                   Horror|Sci-Fi

[3882 rows x 3 columns]
'''
# print(movies.head(1))
'''        첫번째 데이터를 head인지 안다.
   1 Toy Story (1995)   Animation|Children's|Comedy
0  2   Jumanji (1995)  Adventure|Children's|Fantasy
'''

movies = pd.read_csv("../data/movies.dat",sep="::",engine="python",
                     header=None,names=['movieid','title','genre']) # names 은 내가 지정.

print(movies.head(1))
'''
   movieid             title                        genre
0        1  Toy Story (1995)  Animation|Children's|Comedy
'''


