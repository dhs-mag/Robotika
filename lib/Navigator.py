from time import sleep
from threading import Thread


class Navigator:
    # TODO implement here all logic of robot, when steer and etc.
    def __init__(self):
        self.sonar = None
        self.driving = None
        self.threshold = 40.0
        self.thread = None
        self.isRunning = False

    def run(self):
        self.thread = Thread(target=self.start)
        self.thread.setDaemon(True)
        self.thread.start()

    def set_sonar(self, sonar):
        self.sonar = sonar

    def set_driving(self, driving):
        self.driving = driving

    def set_running(self):
        self.isRunning = True

    def start(self):
        while True:
            if self.isRunning:
                distances = self.sonar.get_nav_array()

                left = distances[0] < self.threshold
                center = distances[1] < self.threshold
                right = distances[2] < self.threshold

                # print('left = ', left)
                # print('center = ', center)
                # print('right = ', right)

                if center:
                    if not left and not right:
                        if distances[0] > distances[2]:
                            print('center - left > right')
                            self.driving.left_rotate()
                        else:
                            print('center - right > left')
                            self.driving.right_rotate()
                    elif left and not right:
                        print('left - not right - right rotate')
                        self.driving.right_rotate()
                    elif right and not left:
                        print('right - not left - left rotate')
                        self.driving.left_rotate()
                    else:
                        print('back - rotate back')
                        self.driving.back_rotate()
                elif left:
                    print('turning slow right')
                    self.driving.right()
                elif right:
                    print('turning slow left')
                    self.driving.left()

                else:
                    print('forward')
                    self.driving.forward()

                self.isRunning = False
