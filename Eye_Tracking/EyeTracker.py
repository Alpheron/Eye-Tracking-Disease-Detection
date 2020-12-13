import cv2

from Eye_Tracking.utilities.gaze_tracking import GazeTracking


def gazeTrackingInit(ipAddr):
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(ipAddr)
    return gaze, webcam


def loopMethod(gaze, webcam):
    _, frame = webcam.read()
    gaze.refresh(frame)
    frame = gaze.annotated_frame()
    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    # cv2.imshow("Eye Tracker", frame)
    return [left_pupil, right_pupil]
