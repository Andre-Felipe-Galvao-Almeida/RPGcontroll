#from sklearn import linear_model
from matplotlib import pyplot as plt

y = (0.15, 0.30, 0.75, 1.5, 1.5, 3, 3, 4.5, 4.5, 6, 6, 9, 9)
x = (-4, -3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8)

#dataset = (y, x)

#a = -10
#b = -10


#y == a+b*x

plt.scatter(x, y, color="blue")
plt.xlabel("tamanho")
plt.ylabel("espaço")
plt.show()