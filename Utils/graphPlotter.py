from matplotlib import pyplot as plt

from Utils.GUI.Utils import getScreenDimensions


class Plotter:
    def __init__(self, leftEye, rightEye, target):
        self.leftEye = leftEye
        self.rightEye = rightEye
        self.target = target
        self.plot(self.leftEye, self.rightEye, self.target)

    def getX(self, inputList):
        xList = []
        for x in inputList:
            xList.append(x[0])
        return xList

    def getY(self, inputList):
        yList = []
        for y in inputList:
            yList.append(y[1])
        return yList

    def plot(self, leftEye, rightEye, target):
        plt.plot(self.getX(target), self.getY(target), '-b', label="Target Movement")
        plt.plot(self.getX(leftEye), self.getY(leftEye), '-g', label="Left Eye Movement")
        plt.plot(self.getX(rightEye), self.getY(rightEye), '-r', label="Right Eye Movement")
        plt.legend(loc='best')
        plt.xlim(0, getScreenDimensions()[0])
        plt.ylim(getScreenDimensions()[1], 0)
        plt.show()
