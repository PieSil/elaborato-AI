import random


def getMinimizingValue(var, assignment, problem):
    # checks which color minimizes conflicts if assigned to variable and returns it

    testAssignment = assignment
    minimumConflicts = None
    minValue = assignment[var]

    for color in range(problem.colors):
        testAssignment[var] = color
        currentConflicts, conflicted = problem.conflicts(testAssignment)
        if minimumConflicts is None or currentConflicts < minimumConflicts:
            minimumConflicts = currentConflicts
            minValue = color

    return minValue


def minConflicts(problem, maxSteps, useWeights):
    currentAssignment = AssignmentGenerator(problem.nodes, problem.colors).generate()
    nConflicts, conflictedVars = problem.conflicts(currentAssignment, adjustWeights=False)
    i = 0
    for i in range(maxSteps):
        if nConflicts == 0:
            return currentAssignment, i
        else:
            var = random.choice(list(conflictedVars))
            value = getMinimizingValue(var, currentAssignment, problem)
            currentAssignment[var] = value
            nConflicts, conflictedVars = problem.conflicts(currentAssignment, adjustWeights=useWeights)
    return None, i


class AssignmentGenerator:
    def __init__(self, nodes, colorsNumber):
        self.nodes = nodes
        self.colorsNumber = colorsNumber

    def generate(self):
        # generate random assignment
        assignment = {}
        for node in self.nodes:
            assignment[node.id] = random.randint(0, self.colorsNumber)

        return assignment
