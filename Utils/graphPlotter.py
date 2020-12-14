from matplotlib import pyplot as plt
import cv2
from Utils.GUI.Utils import getScreenDimensions


class Plotter:
    def __init__(self, leftEye, rightEye, target):
        self.leftEye = leftEye
        self.rightEye = rightEye
        self.target = target

    def getX(self, inputList):
        inputList = self.cleanList(inputList)
        print(inputList)
        xList = []
        for x in inputList:
            xList.append(x[0])
        return xList

    def getY(self, inputList):
        inputList = self.cleanList(inputList)
        yList = []
        print(inputList)
        for y in inputList:
            yList.append(y[1])
        return yList

    def cleanList(self, inputList):
        return list(filter(None, inputList))

    def plot(self):
        # plt.plot(self.getX(self.target), self.getY(self.target), '-b', label="Target Movement")
        plt.plot(self.getX(self.leftEye), self.getY(self.leftEye), '-g', label="Left Eye Movement")
        plt.plot(self.getX(self.rightEye), self.getY(self.rightEye), '-r', label="Right Eye Movement")
        plt.legend(loc='best')
        plt.xlim(200, 600)
        plt.ylim(600, 400)
        plt.savefig('/Users/Tinku/Desktop/Eye-Tracking-Disease-Detection/Eye_Tracking/trained_models/test.png')
        self.overLayImages()

    def overLayImages(self):
        normal = cv2.imread("/Users/Tinku/Desktop/Eye-Tracking-Disease-Detection/Eye_Tracking/trained_models/normal.png")
        test = cv2.imread("/Users/Tinku/Desktop/Eye-Tracking-Disease-Detection/Eye_Tracking/trained_models/test.png")
        dst = cv2.addWeighted(normal, 0.3, test, 0.7, 0.0)
        cv2.imshow("Overlay", dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

