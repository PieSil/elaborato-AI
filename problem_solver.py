from utils.result_utility import ResultFileManager
from algorithm.solver import minConflicts
import numpy
import time
from utils.problem_utility import ProblemFileManager
import constants as c

unweightedUnsolved = 0
weightedUnsolved = 0
unweightedSolved = 0
weightedSolved = 0
unweightedSteps = {}
weightedSteps = {}
unweightedTimes = {}
weightedTimes = {}
size = c.START_SIZE
sizes = []
resultManager = ResultFileManager(c.RESULTS_DIR)

for i in range(c.N_DIFFERENT_SIZE_PROBLEMS):
    sizes.append(size)
    size = size + c.SIZE_INCREMENT

problemFileManager = ProblemFileManager()
problems = problemFileManager.loadProblemSet(c.START_SIZE, c.SIZE_INCREMENT, c.N_SAME_SIZE_PROBLEMS,
                                             c.N_DIFFERENT_SIZE_PROBLEMS)

for i in sizes:
    unweightedSteps[i] = []
    weightedSteps[i] = []
    unweightedTimes[i] = []
    weightedTimes[i] = []

problemIndex = 0

for i, problem in enumerate(problems):
    uStartTime = time.time()
    uSolution, uSteps = minConflicts(problem, c.MAX_STEPS, useWeights=False)
    uTotalTime = time.time() - uStartTime
    unweightedSteps[problem.size].append(uSteps)
    unweightedTimes[problem.size].append(uTotalTime)
    if uSolution is not None:
        unweightedSolved = unweightedSolved + 1
    else:
        unweightedUnsolved = unweightedUnsolved + 1

    wStartTime = time.time()
    wSolution, wSteps = minConflicts(problem, c.MAX_STEPS, useWeights=True)
    wTotalTime = time.time() - wStartTime
    weightedSteps[problem.size].append(wSteps)
    weightedTimes[problem.size].append(wTotalTime)
    if wSolution is not None:
        weightedSolved = weightedSolved + 1
    else:
        weightedUnsolved = weightedUnsolved + 1
    print('Problem done, Size = ', problem.size, ', Index = ', i % c.N_SAME_SIZE_PROBLEMS)

unweightedMeanSteps = []
weightedMeanSteps = []
unweightedMeanTimes = []
weightedMeanTimes = []

for i in sizes:
    uMeanExecutionTime = numpy.mean(unweightedTimes[i])
    unweightedMeanTimes.append(uMeanExecutionTime)

    wMeanExecutionTime = numpy.mean(weightedTimes[i])
    weightedMeanTimes.append(wMeanExecutionTime)

    uMeanSteps = numpy.mean(unweightedSteps[i])
    unweightedMeanSteps.append(uMeanSteps)

    wMeanSteps = numpy.mean(weightedSteps[i])
    weightedMeanSteps.append(wMeanSteps)

resultManager.saveResult('sizes.txt', sizes)

resultManager.saveResult('unweighted_mean_times.txt', unweightedMeanTimes)

resultManager.saveResult('weighted_mean_times.txt', weightedMeanTimes)

resultManager.saveResult('unweighted_mean_steps.txt', unweightedMeanSteps)

resultManager.saveResult('weighted_mean_steps.txt', weightedMeanSteps)

resultManager.saveResult('unweighted_solved.txt', [unweightedSolved])

resultManager.saveResult('unweighted_unsolved.txt', [unweightedUnsolved])

resultManager.saveResult('weighted_solved.txt', [weightedSolved])

resultManager.saveResult('weighted_unsolved.txt', [weightedUnsolved])











