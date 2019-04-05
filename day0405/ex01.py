import numpy as np
import pandas as pd

# help를 이용해 파일의 내용을 : 으로 구분하여 바람직하게 읽어 들이도록 합니다.
# print(help(pd.read_csv))
'''
read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal=b'.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)
    Read a comma-separated values (csv) file into DataFrame.
'''

# : 한개로 구분했을 때

''' student 파일 
class:name:kor:eng:mat:bio
1:adam:67:87:90:98
1:andrew:45:45:56:98
1:ben:95:59:96:88
1:clark:65:94:89:98
1:dan:45:65:78:98
1:noel:78:76:98:89
2:paul:87:67:65:56
2:walter:89:98:78:78
2:oscar:100:78:56:65
2:martin:99:89:87:87
2:hugh:98:45:56:54
2:henry:65:89:87:78
'''

df1 = pd.read_csv('../data/student',sep=":")        # student 파일이 csv파일이 아닌데 read_csv 로 읽어 올 수 있다.
df2 = pd.read_csv('../data/student',delimiter=":")
# print(df1)
# print(df2)

''' df1,df2 
        class    name  kor  eng  mat  bio
    0       1    adam   67   87   90   98
    1       1  andrew   45   45   56   98
    2       1     ben   95   59   96   88
    3       1   clark   65   94   89   98
    4       1     dan   45   65   78   98
    5       1    noel   78   76   98   89
    6       2    paul   87   67   65   56
    7       2  walter   89   98   78   78
    8       2   oscar  100   78   56   65
    9       2  martin   99   89   87   87
    10      2    hugh   98   45   56   54
    11      2   henry   65   89   87   78
'''


#  :: 두개로 구분 했을 때

''' student 파일 
class::name::kor::eng::mat::bio
1::adam::67::87::90::98
1::andrew::45::45::56::98
1::ben::95::59::96::88
1::clark::65::94::89::98
1::dan::45::65::78::98
1::noel::78::76::98::89
2::paul::87::67::65::56
2::walter::89::98::78::78
2::oscar::100::78::56::65
2::martin::99::89::87::87
2::hugh::98::45::56::54
2::henry::65::89::87::78
'''


df3 = pd.read_csv('../data/student',sep="::", engine='python')
df4 = pd.read_csv('../data/student',delimiter="::",engine='python')
print(df3)
print(df4)

''' df3,df4 
        class    name  kor  eng  mat  bio
    0       1    adam   67   87   90   98
    1       1  andrew   45   45   56   98
    2       1     ben   95   59   96   88
    3       1   clark   65   94   89   98
    4       1     dan   45   65   78   98
    5       1    noel   78   76   98   89
    6       2    paul   87   67   65   56
    7       2  walter   89   98   78   78
    8       2   oscar  100   78   56   65
    9       2  martin   99   89   87   87
    10      2    hugh   98   45   56   54
    11      2   henry   65   89   87   78
'''
