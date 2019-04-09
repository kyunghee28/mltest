# 예제. x,y 배열을 만들고
# 		x 에는 난수 100개를 발생시켜 담도록 합니다. (단, 난수의 범위는 -1,0,1)
# 		y 에는 x 요소를 누적한 합이 담기도록 합니다.

import  numpy as np
import random

x = np.random.randint(-1,1,100)

for i in len(x):


