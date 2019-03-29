from sklearn import svm,metrics

data = [
    [20, 100, '합격'],
    [18, 3, '불합격'],
    [15, 10, '불합격'],
    [18, 80, '합격'],
    [20, 100, '합격'],
    [18, 0, '불합격'],
    [20, 90, '합격'],
    [17, 50, '불합격'],
    [19, 90, '합격'],
    [14, 50, '불합격']
]

# 70%만 학습에 참여시키고 30%를 갖고 예측하여 정답률을 계산하고 출력하시오.

# 훈련데이터
train_set = data[:7]

# 예측데이터
predic_set = data[7:]


train_data = []
train_label = []
predic_data = []
predic_label = []

# 훈련데이터로 부터 문제와 답을 분리하기
for i in range(len(train_set)):
    row = train_set[i]
    days = row[0]
    hours = row[1]
    ispass = row[2]
    train_data.append([days,hours])
    train_label.append(ispass)
# print(train_data)   [[20, 100], [18, 3], [15, 10], [18, 80], [20, 100], [18, 0], [20, 90]]
# print(train_label)  ['합격', '불합격', '불합격', '합격', '합격', '불합격', '합격']


# 예측을 위한 데이터를 문제와 답으로 분리
for i in range(len(predic_set)):
    row = predic_set[i]
    days = row[0]
    hours = row[1]
    ispass = row[2]
    predic_data.append([days, hours])
    predic_label.append(ispass)
# print(predic_data)   [[17, 50], [19, 90], [14, 50]]
# print(predic_label)   ['불합격', '합격', '불합격']


# 학습시키기
clf = svm.SVC()
clf.fit(train_data, train_label)

# 예측
pre = clf.predict(predic_data)
# print("예측",pre)  -> 예측 ['합격' '합격' '합격']
# print(predic_label) -> ['불합격', '합격', '불합격']

acc = metrics.accuracy_score(predic_label,pre)
print(acc)



