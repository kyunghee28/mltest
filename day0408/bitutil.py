import numpy as np
import pandas as pd

def getMovies():
    movies = pd.read_csv("../data/movies.dat",sep="::",engine="python",
                         header=None,names=['movieid','title','genre'])

    users = pd.read_csv("../data/users.dat",sep="::",engine="python",
                        header=None, names=['userid','gender','age','job','zipcode'])

    ratings = pd.read_csv("../data/ratings.dat",sep="::",engine="python",
                          header=None, names=['userid','movieid','rating','timestamp'])

    df =  pd.merge( pd.merge(movies, ratings), users)

    return df




