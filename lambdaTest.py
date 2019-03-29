# 함수로 만들었을 때
def max(a,b):
    r = a
    if b > r:
        r = b
    return r

print(max(5,3))  #-> 5

# 람다 함수를 사용했을 때
max = lambda a,b: a if a>b else b

print(max(3,6))
print(max(7,1))

# 함수 사용해 더하기
def add(a,b):
    r = a+b
    return r

print(add(5,7))

# 람다를 사용해서 더하기
lambdaadd = lambda a,b: a+b

print(lambdaadd(1,4))
print(lambdaadd(10,4))
