import matplotlib.pyplot as plt

listX = []
listY = []

fig, ax = plt.subplots()
ax.plot(listX, listY)
ax.set_xlabel('X Lable')
ax.set_ylabel('Y Lable')
ax.set_title('My Title')

plt.show()