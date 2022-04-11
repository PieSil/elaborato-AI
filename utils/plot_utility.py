import numpy
import matplotlib.pyplot as plt
import os
import constants as c


def percentageChange(nElements, previous, current):
    valuesPercentageChange = []
    for i in range(nElements):
        change = (previous[i] - current[i]) / (previous[i])
        valuesPercentageChange.insert(i, change * 100)
    return numpy.mean(valuesPercentageChange)


def saveResultGraph(x, y, labels, xlabel, ylabel, fileName, colors, markers):
    path = os.path.join(c.PLOTS_DIR, fileName)
    for i in range(x.shape[0]):
        x_data = x[i].tolist()[0]
        y_data = y[i].tolist()[0]
        plt.plot(x_data, y_data, color=colors[i], label=labels[i], marker=markers[i])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc='best')
    plt.savefig(path)
    plt.clf()
    plt.cla()

def saveResultBar(data, colors, names, fileName):
    path = os.path.join(c.PLOTS_DIR, fileName)
    for i in range(len(data)):
        plt.bar(i, data[i], color=colors[i], width=0.5, label=names[i])
    plt.xticks([])
    plt.legend(loc='best')
    plt.savefig(path)
