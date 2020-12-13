from Eye_Tracking.EyeTracker import gazeTrackingInit
from TestingGUI.EyeCalibration import EyeCalibration
from Utils.graphPlotter import Plotter


def main():
    gaze, webcam = gazeTrackingInit(0)
    eyeCallibrationGUI = EyeCalibration(gaze, webcam)
    graphRender = Plotter(eyeCallibrationGUI.leftEyeCoords, eyeCallibrationGUI.rightEyeCoords,
                          eyeCallibrationGUI.targetCoords)


if __name__ == "__main__":
    main()
