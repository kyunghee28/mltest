import numpy as np

a = np.arange(10)
b = np.arange(10,20)
c = np.arange(10,20,2)
d = np.arange(20,10,-1)
e = np.arange(20,10)

print(a) # [0 1 2 3 4 5 6 7 8 9]
print(b) # [10 11 12 13 14 15 16 17 18 19]
print(c) # [10 12 14 16 18]
print(d) # [20 19 18 17 16 15 14 13 12 11]
print(e) # []  :  거꾸로 갈때는 step 생략 불가능!

