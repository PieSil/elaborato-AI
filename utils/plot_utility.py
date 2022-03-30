import os

class ResultManager:

    def __init__(self, dir):
        self.dir = dir

    def loadResult(self, filename):
        result = []
        path = os.path.join(self.dir, filename)
        with open(path, 'r') as f:
            for line in f:
                result.append(float(line))

        return result

    def saveResult(self, filename, result):
        path = os.path.join(self.dir, filename)
        with open(path, 'w') as f:
            for value in result:
                f.write(str(value) + '\n')
