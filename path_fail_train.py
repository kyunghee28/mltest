from sklearn import svm

data = [
    [20,100,'합격'],
    [18,3,'불합격'],
    [15,10,'불합격'],
    [18,80,'합격'],
    [20,100,'합격'],
    [18,0,'불합격'],
    [20,90,'합격'],
    [17,50,'불합격'],
    [19,90,'합격'],
    [14,50,'불합격']
]

# 70%만 학습에 참여시키고
# 30%를 갖고 예측하여 정답률을 계산하여 출력

time = []
label = []

for row in data:
    s = row[0]
    t = row[1]
    p = row[2]
    time.append([s,t])
    label.append(p)

print(time)
print(label)

clf = svm.SVC()
clf.fit(time[:7],label[:7])

pre = clf.predict(time[7:])
print("예측결과",pre)

ok = 0
total = len(label[7:])
for i in range(len(label[7:])):
    result = label[7:][i]
    p = pre[i]
    print(i,result,p)

    if p == result:
        ok += 1


print("정답률",ok,"/",total,"=",ok/total)
