from sklearn import svm,metrics
import random,re

# 붓꽃의 csv 데이터 읽어 들이기
csv = []
with open('iris.csv','r',encoding='utf-8') as fp:
    # 한줄씩 읽어 들이기
    for line in fp:
        line = line.strip() # 줄바꿈 제거
        cols = line.split(',') # 쉼표로 자르기
        # 문자열 데이터를 숫자로 변환하기
        # 람다식 : 함수가 간단한 경우
        fn = lambda n : float(n) if re.match('^[0-9\.]+$',n) else n
                # 매개변수 n을 전달받아서 if 컨디션(re.match(r'^[0-9\.]+$',n)) 이
                # 참이면 float(n) (숫자로 시작하면 실수로 실행) -> float(n)은 실수

        cols = list(map(fn,cols)) # map이라는 함수가 반복문의 역활을 해준다. / map (함수명, 리스트)

        # 17번째 코드를 풀어쓰면 19~22번째 줄
        # rlist = []
        # for c in cols:
        #     temp = fn(c)
        #     rlist.append(temp)

        # print(cols) 데이터를 한줄 씩 읽어옴,

        csv.append(cols)
# print(csv)  데이터를 2차원 배열에 넣어줌.
        # [['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Name'], [5.1, 3.5, 1.4, 0.2, 'Iris-setosa'],

# 가장 앞 줄의 헤더 제거
del csv[0]
# print(csv) : [[5.1, 3.5, 1.4, 0.2, 'Iris-setosa'], [4.9, 3.0, 1.4, 0.2, 'Iris-setosa'],

# 데이터 셔플하기(섞기) - 붓꽃의 csv 데이터가 중복되어있으닌까 잘 섞어야 한다.
random.shuffle(csv)
# print(csv)

# 학습전용 데이터와 텍스트 전용 데이터 분할하기(2:1 비율)
total_len = len(csv)
train_len = int(total_len * 2/3)
train_data = []
train_label = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

# 데이터를 학습하고 예측하기
clf = svm.SVC()
clf.fit(train_data, train_label)

# print(test_data)

# iris.csv에 있는 정보를 가져와 realDate에 담고 품종 확인
realDate = [[6.4,2.9,4.3,1.3]]
result = clf.predict(realDate)
print(result)
