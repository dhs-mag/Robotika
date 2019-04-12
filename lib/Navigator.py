from time import sleep
from threading import Thread


class Navigator:
#TODO implement here all logic of robot, when steer and etc.
    def __init__(self):
        self.sonar = None
        self.driving = None

    def set_sonar(self, sonar):
        self.sonar = sonar

    def set_driving(self, driving):
        self.driving = driving
