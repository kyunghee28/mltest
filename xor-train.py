from sklearn import svm

# XOR의 계산 결과 데이터
#     XOR연산의 입력과 결과를 2차원 리스트로 정의
xor_data = [
    # 1차원 배열 맨뒤에 있는게 답(라벨)
    [0,0,0],  #0하고 0이들어 가면 답이 0이야
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

# 데이터(문제)와 레이블(답) 분리하기
data =[]
label = []

for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p,q])
    label.append([r])

# print(data) : [[0, 0], [0, 1], [1, 0], [1, 1]]
# print(label) : [[0], [1], [1], [0]]

# 데이터 학습시키기
clf = svm.SVC()
clf.fit(data,label) # fit() 메소들르 새용해 데이터를 학습시킨다.

# 데이터 예측하기
# predict() 메서드에 예측하고 싶은 데이터 배열을 전달하면 데이터 수만큼 예측결과를 리턴해준다.
pre = clf.predict(data)
    # 학습시킨 데이터 그대로 예측
    # 원래는 30%정도의 데이터로 예측
print("예측결과",pre) # 예측결과 [0 1 1 0]

# 결과확인하기 - 예측결과가 정답과 맞는지 확인
# ok = 0; total = 0;
# for idx,answer in enumerate(label): label을 answer에 담고 idx도 필요해.
#     p = pre[idx]
#     if p == answer: ok += 1
#     total += 1

ok = 0
total = len(label)
for i in range(len(label)):
    answer = label[i]
    p = pre[i]
    if answer == p:
      ok += 1

print("정답률",ok,"/",total,"=",ok/total)  #정답률 4 / 4 = 1.0(100%)