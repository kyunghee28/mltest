from sklearn import svm

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
score = []
label = []
for row in data:
    d = row[0]
    t = row[1]
    r = row[2]
    score.append([d,t])
    label.append(r)

clf = svm.SVC()
clf.fit(score[0:7], label[0:7])
pre = clf.predict(score[7:10])
print(pre)

ok = 0
total = len(label[7:10])
for i in range(len(label[7:10])):
    answer = label[7:10][i]
    p = pre[i]
    print(i, answer, p)

    if answer == p:
        ok += 1

print("정답률: ",ok,"/",total,"=", ok/total)