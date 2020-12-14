import cv2

from Utils.EyeTracking.gaze_tracking import GazeTracking
from Utils.GUI.Utils import getScreenDimensions


def gazeTrackingInit(ipAddr):
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(ipAddr)
    return gaze, webcam


def loopMethod(gaze, webcam):
    _, frame = webcam.read()
    gaze.refresh(frame)
    frame = gaze.annotated_frame()
    if gaze.pupil_left_coords() is not None:
        left_pupil = [
            gaze.pupil_left_coords()[0] - (webcam.get(cv2.CAP_PROP_FRAME_WIDTH) / 2 - getScreenDimensions()[0] / 2),
            gaze.pupil_left_coords()[1] / webcam.get(cv2.CAP_PROP_FRAME_HEIGHT) * getScreenDimensions()[1]]
    else:
        left_pupil = None
    if gaze.pupil_right_coords() is not None:
        right_pupil = [
            gaze.pupil_right_coords()[0] - (webcam.get(cv2.CAP_PROP_FRAME_WIDTH) / 2 - getScreenDimensions()[0] / 2),
            gaze.pupil_right_coords()[1] / webcam.get(cv2.CAP_PROP_FRAME_HEIGHT) * getScreenDimensions()[1]]
    else:
        right_pupil = None
    # cv2.imshow("Eye Tracker", frame)
    return [left_pupil, right_pupil]
