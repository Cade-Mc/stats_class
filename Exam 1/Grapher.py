import numpy as np
import matplotlib.pyplot as plt
import STD

listranges = []
numbers = []

STD.innumbs()

lower_lims = []
upper_lims = []

STD.limits()
STD.standard_dev()
STD.rangecount()

print(listranges)
yaxis = listranges

def bargraph():
    x = np.array(upper_lims)
    print(x)
    y = np.array(yaxis)
    print(y)
    plt.xlabel("Ranges")
    plt.ylabel("Frequency")
    plt.bar(x, y)
    plt.show()


bargraph()

def linegraph():
    x = np.array(upper_lims)
    print(x)
    y = np.array(yaxis)
    print(y)
    plt.xlabel("Ranges")
    plt.ylabel("Frequency")
    plt.bar(x, y)
    plt.plot(x, y)
    plt.show()


linegraph()