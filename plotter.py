import numpy
import matplotlib.pyplot as plt
import constants as c
from utils.result_utility import ResultFileManager
import os

resultManager = ResultFileManager(c.RESULTS_DIR)

sizes = resultManager.loadResult('sizes.txt')
unweightedUnsolved = resultManager.loadResult('unweighted_unsolved.txt')[0]
weightedUnsolved = resultManager.loadResult('weighted_unsolved.txt')[0]
unweightedSolved = resultManager.loadResult('unweighted_solved.txt')[0]
weightedSolved = resultManager.loadResult('weighted_solved.txt')[0]

unweightedMeanSteps = resultManager.loadResult('unweighted_mean_steps')
weightedMeanSteps = resultManager.loadResult('weighted_mean_steps')
unweightedMeanTimes = resultManager.loadResult('unweighted_mean_times')
weightedMeanTimes = resultManager.loadResult('weighted_mean_times')

barNames = ['Unweighted Solved', 'Unweighted Unsolved', 'Weighted Solved', 'Weighted Unsolved']
solvedData = [unweightedSolved, unweightedUnsolved, weightedSolved, weightedUnsolved]
barColors = ['red', 'maroon', 'green', 'darkgreen']

plt.figure(0)
plt.plot(sizes, unweightedMeanTimes, 'r', label='unweighted', marker='o')
plt.plot(sizes, weightedMeanTimes, 'g', label='weighted', marker='o')
plt.ylim(-0.05, numpy.max(unweightedMeanTimes) + 0.5)
plt.xlabel('Size')
plt.ylabel('Time in seconds (mean)')
plt.legend(loc='best')
path = os.path.join(c.PLOTS_DIR, 'mean_times.png')
plt.savefig(path)

plt.figure(1)
plt.plot(sizes, unweightedMeanTimes, 'r', label='unweighted', marker='o')
plt.plot(sizes, weightedMeanTimes, 'g', label='weighted', marker='o')
plt.ylim(-0.05, numpy.max(unweightedMeanTimes) + 0.5)
for i in range(len(sizes)):
    if i % 5 == 0:
        x = sizes[i]
        y = unweightedMeanTimes[i]
        plt.annotate(str('%.3f'%y), (x+0.05, y+0.05), color='maroon')
for i in range(len(sizes)):
    if i % 5 == 0:
        x = sizes[i]
        y = weightedMeanTimes[i]
        plt.annotate(str('%.3f'%y), (x-0.05, y-0.05))
plt.xlabel('Size')
plt.ylabel('Time in seconds (mean)')
plt.legend(loc='best')
path = os.path.join(c.PLOTS_DIR, 'mean_times_noted.png')
plt.savefig(path)

plt.figure(2)
plt.plot(sizes, unweightedMeanSteps, 'r', label='unweighted', marker='o')
plt.plot(sizes, weightedMeanSteps, 'g', label='weighted', marker='o')
plt.xlabel('Size')
plt.ylabel('Number of steps (mean)')
plt.legend(loc='best')
path = os.path.join(c.PLOTS_DIR, 'mean_steps.png')
plt.savefig(path)

plt.figure(3)
plt.plot(sizes, unweightedMeanSteps, 'r', label='unweighted', marker='o')
plt.plot(sizes, weightedMeanSteps, 'g', label='weighted', marker='o')
for i in range(len(sizes)):
    if i % 5 == 0:
        x = sizes[i]
        y = unweightedMeanSteps[i]
        plt.annotate(str(y), (x+0.05, y+100), color='maroon')
for i in range(len(sizes)):
    if i % 5 == 0:
        x = sizes[i]
        y = weightedMeanSteps[i]
        plt.annotate(str(y), (x-0.05, y-100))
plt.xlabel('Size')
plt.ylabel('Number of steps (mean)')
plt.legend(loc='best')
path = os.path.join(c.PLOTS_DIR, 'mean_steps_noted.png')
plt.savefig(path)

plt.figure(4)
plt.bar(1, solvedData[0], color=barColors[0], width=0.5, label=barNames[0])
plt.bar(2, solvedData[1], color=barColors[1], width=0.5, label=barNames[1])
plt.bar(3, solvedData[2], color=barColors[2], width=0.5, label=barNames[2])
plt.bar(4, solvedData[3], color=barColors[3], width=0.5, label=barNames[3])
plt.xticks([])
plt.legend(loc='best')
path = os.path.join(c.PLOTS_DIR, 'solved_bar_graph.png')
plt.savefig(path)