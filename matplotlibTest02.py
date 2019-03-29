import matplotlib.pyplot as plt

for i in range(-10,11):
    print(i)
    plt.plot(i,i**2,'mo')

plt.xlim(-10,10)
plt.ylim(-5,10)
plt.show()

