import numpy

from algorithm.node import Node
from utils.segment_functions import intersects


class Problem:
    def __init__(self, n, colorsNumber):
        self.max_neighs = int(numpy.sqrt(n))
        self.colors = colorsNumber
        self.size = n
        self.nodes = []
        self.edges = []
        self.edgeWeights = {}

    def build(self):
        self.scatterNodes()

        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1 != node2 and not node1.isNeighbour(node2) and len(node1.neighbours) < self.max_neighs and len(
                        node2.neighbours) < self.max_neighs:
                    edge_intersects = False

                    for edge in self.edges:
                        if not edge_intersects and intersects(node1, node2, edge[0], edge[1]):
                            edge_intersects = True

                    if not edge_intersects:
                        self.edges.append((node1, node2))
                        node1.addNeighbour(node2)
                        node2.addNeighbour(node1)

        for edge in self.edges:
            self.edgeWeights[edge] = 1

    def scatterNodes(self):

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

    def calculateConflicts(self, assignment, adjustWeights=False):
        nConflicts = 0
        conflicted = set()
        for edge in self.edges:
            if assignment[edge[0].id] == assignment[edge[1].id]:
                nConflicts = nConflicts + self.edgeWeights[edge]
                conflicted.add(edge[0].id)
                conflicted.add(edge[1].id)
                if adjustWeights:
                    self.edgeWeights[edge] = self.edgeWeights[edge] + 1

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