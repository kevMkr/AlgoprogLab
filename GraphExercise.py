import matplotlib.pyplot as plt
import numpy as np

datapoints = int(input("Enter Data Points:"))
graphtype = input("Scatter,Plot, or Bar:")

temp = []
for i in range(datapoints+1):
    temp.append(i)

x = np.array(temp)

temp = []
for i in range(datapoints+1):
    temp.append(i**2)


y = np.array(temp)

if graphtype == "Scatter":
    plt.scatter(x,y)

    plt.show()

if graphtype == "Plot":
    plt.plot(x,y)

    plt.show()

if graphtype == "Bar":
    plt.bar(x,y)

    plt.show()

