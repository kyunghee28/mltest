# 연습 ) Data폴더의 user.dat, movies.dat, ratings,dat 파일을 읽어들어
# 하나의 DataFrame으로 만들어 봅시다.

#movies.dat
# 영화id::영화제목::장르
# movieid::title::genre
# 1::Toy Story (1995)::Animation|Children's|Comedy

#users.dat
#사용자id::성별::나이::직업::우편번호
#userid::gender::age::job::zipcode
# 1::F::1::10::48067

#rating.dat
#사용자id::영화id::별점::시간
#userid::movieid::rating::timestamp
# 1::1193::5::978300760

''' 서로 공통이 있는 것으로 합칠 수 있다!!
movies.dat 과 rating.dat 은 movieid 가 공통
users.dat 과 rating.dat 은 userid가 공통
'''

import numpy as np
import pandas as pd

# help를 이용하여
# 파일을 읽어 들일때 컬럼헤더는 없다라는 옵션을 설정하고
# 칼럼이름을 읽어들이때 movieId, title, genre 설정하도록 해 봅니다.
# help(pd.read_csv)

movies = pd.read_csv("../data/movies.dat",sep="::",engine="python",
                     header=None,names=['movieid','title','genre']) # names 은 내가 지정.

# print(movies.head(1))
#    movieid             title                        genre
# 0        1  Toy Story (1995)  Animation|Children's|Comedy

users = pd.read_csv("../data/users.dat",sep="::",engine="python",
                    header=None, names=['userid','gender','age','job','zipcode'])

# print(users.head(1))
#    userid gender  age  job zipcode
# 0       1      F    1   10   48067

ratings = pd.read_csv("../data/ratings.dat",sep="::",engine="python",
                      header=None, names=['userid','movieid','rating','timestamp'])

# print(ratings.head(1))
#    userid  movieid  rating  timestamp
# 0       1     1193       5  978300760

# print(movies)
# 3880     3950  ...                           Drama
# 3881     3951  ...                           Drama
# 3882     3952  ...                  Drama|Thriller
#
# [3883 rows x 3 columns]

# print(users)
# 6037    6038      F   56    1   14706
# 6038    6039      F   45    0   01060
# 6039    6040      M   25    6   11106
#
# [6040 rows x 5 columns]

# print(ratings)
#
# 1000205    6040     1094       5  956704887
# 1000206    6040      562       5  956704746
# 1000207    6040     1096       4  956715648
# 1000208    6040     1097       4  956715569
#
# [1000209 rows x 4 columns]


# 하나의 DataFrame으로 만들기 => merge
# 공통으로 들어가는 속성이 있어야 합칠 수 있다.(오라클의 join)

r = pd.merge(movies, ratings)
# print(r.head(1))
#    movieid             title  ... rating  timestamp
# 0        1  Toy Story (1995)  ...      5  978824268
#
# [1 rows x 6 columns]


df =  pd.merge( pd.merge(movies, ratings), users)   # 3개의 객체가 합쳐짐.
# print(df.head(1))
'''
   movieid             title                        genre  ...  age  job  zipcode
0        1  Toy Story (1995)  Animation|Children's|Comedy  ...    1   10    48067

[1 rows x 10 columns]
'''




