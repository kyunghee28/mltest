import numpy as np
import pandas as pd

def getMovies():    # 3개의 파일(movies,users,ratings)을 하나의 DataFrame으로 반환하는 함수
    movies = pd.read_csv("../data/movies.dat",sep="::",engine="python",
                         header=None,names=['movieid','title','genre'])

    users = pd.read_csv("../data/users.dat",sep="::",engine="python",
                        header=None, names=['userid','gender','age','job','zipcode'])

    ratings = pd.read_csv("../data/ratings.dat",sep="::",engine="python",
                          header=None, names=['userid','movieid','rating','timestamp'])

    df =  pd.merge( pd.merge(movies, ratings), users)

    return df

def get_500_Movies():   # 평가한 사람의 수가 500 건 이상인 영화의 건수를 기분으로 내림차순으로 정렬하여 반환

    df = getMovies()
    title_count = df.pivot_table(values='rating', index='title', aggfunc='count')

    title_500 = title_count[title_count['rating'] >= 500]

    title_500_sort = title_500.sort_values(by='rating', ascending='False')

    return  title_500_sort

