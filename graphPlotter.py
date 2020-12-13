from matplotlib import pyplot as plt


class Plotter:
    def __init__(self, leftEye, rightEye, target):
        self.leftEye = leftEye
        self.rightEye = rightEye
        self.target = target

    def getXY(self, inputList):
        xList = []
        yList = []
        for x in inputList:
            xList.append(x[0])
            yList.append(x[1])
        return [xList, yList]

    def plot(self, xList, yList):
