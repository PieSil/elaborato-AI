class Node:
    def __init__(self, x, y, id):
        self.id = id
        self.x = x
        self.y = y
        self.neighbours = set()

    def isNeighbour(self, node):
        result = False
        if node in self.neighbours:
            result = True

        return result

    def addNeighbour(self, node):
        self.neighbours.add(node)

    def printNeighbours(self):
        print('Neighbours: ', end="")
        for neighbour in self.neighbours:
            print(neighbour.id, end=" ")
