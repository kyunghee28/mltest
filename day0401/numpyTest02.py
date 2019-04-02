import numpy as np

a = [0,1,2,3,4]

b = np.arange(5)

c = list(b)

d = np.array(a)

# list -> np.array(리스트를 넘파이 배열로 바꾸기) : np.array
# np.array -> list (넘파이 배열을 리스트로 바꾸기) : list

print(a) # [0, 1, 2, 3, 4]
print(b) # [0 1 2 3 4]
print(c)  # [0, 1, 2, 3, 4]
print(d) # [0 1 2 3 4]

print(type(a)) # <class 'list'>
print(type(b)) # <class 'numpy.ndarray'>
print(type(c)) #<class 'list'>
print(type(d)) #<class 'numpy.ndarray'>