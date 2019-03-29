import matplotlib.pyplot as plt

age = [28,16,40,30,20,29,28,17]
height = [180,159,145,176,164,193,160,171]

plt.plot(age,height,"ms")
plt.xlim(10,50)
plt.ylim(130,200)
plt.show()

def nou_used():
    data = [28,16,40,30,20,29,28,17]

    plt.plot(data)
    plt.show()