from Eye_Tracking.EyeTracker import gazeTrackingInit
from TestingGUI.EyeCalibration import EyeCalibration


def main():
    gaze, webcam = gazeTrackingInit(0)
    eyeCallibrationGUI = EyeCalibration(gaze, webcam)
    print(eyeCallibrationGUI.leftEyeCoords)
    print(eyeCallibrationGUI.rightEyeCoords)


if __name__ == "__main__":
    main()
