import numpy
import random
from algorithm.node import Node
from utils.segment_functions import intersects
import os
import constants as c


class Problem:
    def __init__(self, n, colorsNumber):
        self.max_neighs = int(numpy.sqrt(n))
        self.colors = colorsNumber
        self.size = n
        # self.assignment = {}
        self.nodes = []
        self.edges = []
        self.edgeWeights = {}

    def build(self):
        self.scatterNodes()

        # print('Creating edges... ')
        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1 != node2 and not node1.isNeighbour(node2) and len(node1.neighbours) < self.max_neighs and len(
                        node2.neighbours) < self.max_neighs:
                    edge_intersects = False

                    for edge in self.edges:
                        if not edge_intersects and intersects(node1, node2, edge[0], edge[1]):
                            edge_intersects = True
                            # print('Could not generate edge between following nodes: ')
                            # print('Node ', node1.id, ':', '{', node1.x, ', ', node1.y, '}')
                            # print('Node ', node2.id, ':', '{', node2.x, ', ', node2.y, '}')

                            # print('Because in intersects with following edge: ')
                            # print('Node ', edge[0].id, ':', '{', edge[0].x, ', ', edge[0].y, '}')
                            # print('Node ', edge[1].id, ':', '{', edge[1].x, ', ', edge[1].y, '}')
                            # print('---------------------------------------------')

                    if not edge_intersects:
                        self.edges.append((node1, node2))
                        node1.addNeighbour(node2)
                        node2.addNeighbour(node1)

        for edge in self.edges:
            self.edgeWeights[edge] = 1

        # print('Edges created: ')
        # for node in self.nodes:
            # print('Node ', node.id, ' ', end=" ")
            # node.printNeighbours()
            # print()

    def scatterNodes(self):
        # print('Scattering nodes...')

        used_coords = {}  # avoids using same coordinates for two different nodes

        for id in range(self.size):
            # generate random coordinates for a node
            coord = tuple(numpy.random.uniform(size=2))

            # check if a node with same coordinates already exists
            while coord in used_coords:
                coord = tuple(numpy.random.uniform(size=2))

            # create node with given coordinates
            self.nodes.insert(id, (Node(coord[0], coord[1], id)))
            used_coords[coord] = self.nodes[id]

        # print('Nodes scattered: ')
        # for node in self.nodes:
            # print('Node ', node.id, ': ', end="")
            # print('(', node.x, ', ', node.y, ')')

    def calculateConflicts(self, assignment, adjustWeights=False, printConflicts=False):
        nConflicts = 0
        conflicted = set()
        for edge in self.edges:
            isConflicted = False
            if assignment[edge[0].id] == assignment[edge[1].id]:
                nConflicts = nConflicts + self.edgeWeights[edge]
                conflicted.add(edge[0].id)
                conflicted.add(edge[1].id)
                isConflicted = True
            if adjustWeights:
                if isConflicted:
                    self.edgeWeights[edge] = self.edgeWeights[edge] + 1
                #else:
                #    newWeight = self.edgeWeights[edge] - 1
                 #   if newWeight > 0:
                 #       self.edgeWeights[edge] = newWeight

       #  if printConflicts:
            # for edge in self.edgeWeights.keys():
                # print('Edge: (', edge[0].id, ', ', edge[1].id, '), Weight: ',  self.edgeWeights[edge])

        return nConflicts, conflicted

    def toString(self):
        result = 'Problem description:\n'
        result = result + 'Number of nodes: ' + str(self.size) + '\n'
        result = result + 'Number of colors: ' + str(self.colors) + '\n'

        for node in self.nodes:
            result =  result + 'Node id: ' + str(node.id)
            result = result + ', Neighbours: '
            for neigh in node.neighbours:
                result = result + str(neigh.id) + ', '
            result = result + '\n'

        result = result + 'Edges:\n'
        for edge in self.edges:
            result = result + '(' + str(edge[0].id) + ', ' + str(edge[1].id) + ')' + '\n'
        result = result + '------------------\n'

        return result


class AssignmentGenerator:
    def __init__(self, nodes, colorsNumber):
        self.nodes = nodes
        self.colorsNumber = colorsNumber

    def generate(self):
        # generate random assignment
        assignment = {}
        # print('Generating random assignment... ')
        for node in self.nodes:
            assignment[node.id] = random.randint(0, self.colorsNumber)

        # print("Random assignment generated: ")
        # for node in assignment.keys():
            # print("Node: ", node, " Color: ", assignment[node])

        return assignment


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

        print('Problem saved in ', path)

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
