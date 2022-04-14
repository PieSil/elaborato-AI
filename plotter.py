import numpy
import constants as c
from utils.result_utility import ResultFileManager
import os
from utils.plot_utility import percentageChange
from utils.plot_utility import saveResultGraph
from utils.plot_utility import saveResultBar

resultManager = ResultFileManager(c.RESULTS_DIR)

# load results from .txt files
sizes = resultManager.loadResult('sizes.txt')
unweightedUnsolved = resultManager.loadResult('unweighted_unsolved.txt')[0]
weightedUnsolved = resultManager.loadResult('weighted_unsolved.txt')[0]
unweightedSolved = resultManager.loadResult('unweighted_solved.txt')[0]
weightedSolved = resultManager.loadResult('weighted_solved.txt')[0]
unweightedMeanSteps = resultManager.loadResult('unweighted_mean_steps.txt')
weightedMeanSteps = resultManager.loadResult('weighted_mean_steps.txt')
unweightedMeanTimes = resultManager.loadResult('unweighted_mean_times.txt')
weightedMeanTimes = resultManager.loadResult('weighted_mean_times.txt')

# calculate and print mean percentage change of execution times and number of steps
meanTimesPC = percentageChange(len(sizes), unweightedMeanTimes, weightedMeanTimes)
meanStepsPC = percentageChange(len(sizes), unweightedMeanSteps, weightedMeanSteps)
print('Mean execution times percentage change ', meanTimesPC)
print('Mean number of steps percentage change: ', meanStepsPC)

# plot results on graphs
barNames = ['Unweighted Solved', 'Unweighted Unsolved', 'Weighted Solved', 'Weighted Unsolved']
solvedData = [unweightedSolved, unweightedUnsolved, weightedSolved, weightedUnsolved]
barColors = ['red', 'maroon', 'green', 'darkgreen']
graphLabels = ['unweighted', 'weighted']
graphColors = ['red', 'green']
graphMarkers = ['o', 'o']

saveResultGraph(numpy.matrix([sizes, sizes]), numpy.matrix([unweightedMeanTimes, weightedMeanTimes]),
                labels=graphLabels, colors=graphColors, xlabel='Size', ylabel='Time in seconds (mean)',
                markers=graphMarkers, fileName='mean_times.png')

saveResultGraph(numpy.matrix([sizes, sizes]), numpy.matrix([unweightedMeanSteps, weightedMeanSteps]),
                labels=graphLabels, colors=graphColors, xlabel='Size', ylabel='Number of steps (mean)',
                markers=graphMarkers, fileName='mean_steps.png')

saveResultBar(solvedData, colors=barColors, names=barNames, fileName='solved_bar_graph.png')