import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def makeChart(name):
    df = pd.read_csv("data/scores.csv")
    df.index = df['name']
    del df['name']

    try:
        subject = ['kor', 'eng', 'mat', 'bio']
        rc("font",family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())
        plt.bar(range(len(subject)), df.loc[name][subject] )
        plt.title(name+" 의 과목별 점수")
        plt.xticks(range(len(subject)),subject)
        fname = 'static/'+name+'.png'
        plt.savefig(fname)
        plt.close()
        print('차트를 만들었어요')
    except KeyError:
        fname = 'no'
    return fname
