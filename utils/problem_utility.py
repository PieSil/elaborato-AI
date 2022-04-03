from algorithm.node import Node
from algorithm.problem import Problem
import os
import constants as c


class ProblemFileManager:

    def saveProblem(self, problem, filename):

        path = os.path.join(c.CSP_DIR, filename)

        with open(path, 'w') as f:
            f.write(str(problem.size) + '\n')
            f.write(str(problem.colors) + '\n')
            for node in problem.nodes:
                nodeData = str(node.id) + ', ' + str(node.x) + ', ' + str(node.y) + '\n'
                f.write(nodeData)
                # for neighbour in node.neighbours:
                    # f.write(str(neighbour.id) + ', ')
                # f.write('\n')
            f.write('end_nodes\n')
            for edge in problem.edges:
                edgeData = str(edge[0].id) + ', ' + str(edge[1].id) + '\n'
                f.write(edgeData)
            f.write('end')

        print('Problem saved to ', path)

    def loadProblem(self, filename):
        problem = None
        path = os.path.join(c.CSP_DIR, filename)
        with open(path, 'r') as f:
            problemSize = int(f.readline())
            problemColors = int(f.readline())
            problem = Problem(problemSize, problemColors)
            node = f.readline().split(', ')
            while node[0] != 'end_nodes\n':
                id = int(node[0])
                x = float(node[1])
                y = float(node[2])
                problem.nodes.insert(id, Node(x, y, id))
                node = f.readline().split(', ')

            edgeLine = f.readline().split(', ')
            while edgeLine[0] != 'end':
                firstEdgeId = int(edgeLine[0])
                secondEdgeId = int(edgeLine[1])
                problem.edges.append((problem.nodes[firstEdgeId], problem.nodes[secondEdgeId]))
                problem.nodes[firstEdgeId].addNeighbour(problem.nodes[secondEdgeId])
                problem.nodes[secondEdgeId].addNeighbour(problem.nodes[firstEdgeId])
                edgeLine = f.readline().split(', ')

        for edge in problem.edges:
            problem.edgeWeights[edge] = 1

        print('Problem loaded: ' + path)
        return problem

    def generateProblemSet(self, startSize, sizeIncrement, nSameSizeProblems, maxProblemRange, nColors=4):
        size = startSize
        sizes = []

        for i in range(maxProblemRange):
            sizes.append(size)
            size = size + sizeIncrement

        for i in sizes:
            for j in range(nSameSizeProblems):
                newProblem = Problem(i, nColors)
                newProblem.build()
                self.saveProblem(newProblem, ('csp_' + str(i) + '_' + str(j) + '.txt'))

                print('Problem Created, Size = ', i)

    def loadProblemSet(self, startSize, sizeIncrement, nSameSizeProblems, maxProblemRange):
        size = startSize
        sizes = []
        problems = []

        for i in range(maxProblemRange):
            sizes.append(size)
            size = size + sizeIncrement

        for i in sizes:
            for j in range(nSameSizeProblems):
                problems.append(self.loadProblem('csp_' + str(i) + '_' + str(j) + '.txt'))

        return problems
