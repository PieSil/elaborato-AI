from utils.problem_utility import AssignmentGenerator
import random


def getMinimizingValue(var, assignment, problem):
    testAssignment = assignment
    minimumConflicts = None
    minValue = assignment[var]

    for color in range(problem.colors):
        testAssignment[var] = color
        currentConflicts, conflicted = problem.calculateConflicts(testAssignment)
        if minimumConflicts is None or currentConflicts < minimumConflicts:
            minimumConflicts = currentConflicts
            minValue = color

    return minValue


def minConflicts(problem, maxSteps, useWeights):
    currentAssignment = AssignmentGenerator(problem.nodes, problem.colors).generate()
    nConflicts, conflictedVars = problem.calculateConflicts(currentAssignment, False, True)
    i = 0
    for i in range(maxSteps):
        # print('Iteration: ', i, ' Number of conflicts: ', nConflicts)
        if nConflicts == 0:
            return currentAssignment, i
        else:
            var = random.choice(list(conflictedVars))
            value = getMinimizingValue(var, currentAssignment, problem)
            currentAssignment[var] = value
            nConflicts, conflictedVars = problem.calculateConflicts(currentAssignment, useWeights, True)
    return None, i
