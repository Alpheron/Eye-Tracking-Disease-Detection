import time

import pygame

from Eye_Tracking.EyeTracker import loopMethod
from TestingGUI.Sprites.Background import Background
from TestingGUI.Sprites.Target import Target
from TestingGUI.Utils.Utils import getScreenDimensions, quitLoopConditional, init


class EyeCalibration:
    def __init__(self, gaze, webcam):
        self.screen = pygame.display.set_mode(getScreenDimensions())
        init()
        self.clock = pygame.time.Clock()
        self.background = Background(self.screen)
        self.target = Target(self.screen)
        self.isRunning = False
        self.leftEyeCoords = []
        self.rightEyeCoords = []
        self.targetCoords = []
        pygame.init()
        self.calibrationRoutine(gaze, webcam)

    def calibrationRoutine(self, gaze, webcam):
        self.isRunning = True
        ticks = 0
        start = time.time()
        while self.isRunning:
            self.background.fill([0, 255, 0])
            self.target.followPath(ticks)
            self.targetCoords.append(list(self.target.rect.center))
            eyeCoords = loopMethod(gaze, webcam)
            self.leftEyeCoords.append(eyeCoords[0])
            self.rightEyeCoords.append(eyeCoords[1])
            ticks = self.clock.tick_busy_loop(60)
            pygame.display.flip()
            quitLoopConditional(self.isRunning)
            if self.target.finalDestReached:
                end = time.time()
                print(end - start)
                break


if __name__ == '__main__':
    exception = EyeCalibration()
