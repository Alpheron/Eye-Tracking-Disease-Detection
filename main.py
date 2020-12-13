from Eye_Tracking.EyeTracker import gazeTrackingInit
from TestingGUI.EyeCalibration import EyeCalibration


def main():
    gaze, webcam = gazeTrackingInit("http://10.74.1.103:4747/video")
    eyeCallibrationGUI = EyeCalibration(gaze, webcam)
    print(eyeCallibrationGUI.leftEyeCoords)
    print(eyeCallibrationGUI.rightEyeCoords)


if __name__ == "__main__":
    main()
