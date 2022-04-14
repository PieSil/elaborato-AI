import os

class ResultFileManager:

    def __init__(self, dir):
        self.dir = dir

    def loadResult(self, filename):
        # loads a list of floats from a .txt file

        result = []
        path = os.path.join(self.dir, filename)
        with open(path, 'r') as f:
            for line in f:
                result.append(float(line))

        return result

    def saveResult(self, filename, result):
        # saves a list of floats to a .txt file

        path = os.path.join(self.dir, filename)
        with open(path, 'w') as f:
            for value in result:
                f.write(str(value) + '\n')
