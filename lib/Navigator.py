from threading import Thread
from ev3dev2.led import LED_COLORS, Leds, LED_GROUPS


class Navigator:
    # TODO implement here all logic of robot, when steer and etc.
    def __init__(self):
        self.sonar = None
        self.driving = None
        self.threshold = 40.0
        self.thread = None
        self.isRunning = False
        self.system_run = True
        self.is_started = False
        self.leds = Leds()

    def __del__(self):
        self.system_run = False

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

    def start_nav(self):
        print("Start running")
        self.is_started = True

    def stop_nav(self):
        print("Stop running")
        self.is_started = False
        self.driving.stop()
        self.leds.set_color('LEFT', "GREEN")
        self.leds.set_color('RIGHT', "GREEN")

    def start(self):
        while self.system_run:
            if self.is_started and self.isRunning:
                distances = self.sonar.get_nav_array()

                left = distances[0] < self.threshold
                center = distances[1] < self.threshold
                right = distances[2] < self.threshold

                if center:
                    if not left and not right:
                        if distances[0] > distances[2]:
                            print('center - left > right')
                            self.leds.set_color('LEFT', "RED")
                            self.leds.set_color('RIGHT', "GREEN")
                            self.driving.left_rotate()
                        else:
                            print('center - right > left')
                            self.leds.set_color('LEFT', "GREEN")
                            self.leds.set_color('RIGHT', "RED")
                            self.driving.right_rotate()
                    elif left and not right:
                        print('left - not right - right rotate')
                        self.leds.set_color('LEFT', "GREEN")
                        self.leds.set_color('RIGHT', "RED")
                        self.driving.right_rotate()
                    elif right and not left:
                        print('right - not left - left rotate')
                        self.leds.set_color('LEFT', "RED")
                        self.leds.set_color('RIGHT', "GREEN")
                        self.driving.left_rotate()
                    else:
                        print('back - rotate back')
                        self.leds.set_color('LEFT', "RED")
                        self.leds.set_color('RIGHT', "RED")
                        self.driving.right_rotate()
                elif left:
                    print('turning slow right')
                    self.leds.set_color('LEFT', "GREEN")
                    self.leds.set_color('RIGHT', "ORANGE")
                    self.driving.right()
                elif right:
                    print('turning slow left')
                    self.leds.set_color('LEFT', "ORANGE")
                    self.leds.set_color('RIGHT', "GREEN")
                    self.driving.left()

                else:
                    print('forward')
                    self.leds.set_color('LEFT', "GREEN")
                    self.leds.set_color('RIGHT', "GREEN")
                    self.driving.forward()

                self.isRunning = False
