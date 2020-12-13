from matplotlib import pyplot as plt

from Utils.GUI.Utils import getScreenDimensions


class Plotter:
    def __init__(self, leftEye, rightEye, target):
        self.leftEye = leftEye
        self.rightEye = rightEye
        self.target = target

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

    def plot(self):
        plt.plot(self.getX(self.target), self.getY(self.target), '-b', label="Target Movement")
        plt.plot(self.getX(self.leftEye), self.getY(self.leftEye), '-g', label="Left Eye Movement")
        plt.plot(self.getX(self.rightEye), self.getY(self.rightEye), '-r', label="Right Eye Movement")
        plt.legend(loc='best')
        plt.xlim(0, getScreenDimensions()[0])
        plt.ylim(getScreenDimensions()[1], 0)
        plt.show()
