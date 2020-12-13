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
    left_pupil = [
        gaze.pupil_left_coords()[0] - (webcam.get(cv2.CAP_PROP_FRAME_WIDTH) / 2 - getScreenDimensions()[0] / 2),
        gaze.pupil_left_coords()[1] / webcam.get(cv2.CAP_PROP_FRAME_HEIGHT) * getScreenDimensions()[0]]
    right_pupil = [
        gaze.pupil_right_coords()[0] - (webcam.get(cv2.CAP_PROP_FRAME_WIDTH) / 2 - getScreenDimensions()[0] / 2),
        gaze.pupil_right_coords()[1] / webcam.get(cv2.CAP_PROP_FRAME_HEIGHT) * getScreenDimensions()[0]]
    # cv2.imshow("Eye Tracker", frame)
    return [left_pupil, right_pupil]
