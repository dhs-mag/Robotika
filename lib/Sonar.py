from time import sleep
from threading import Thread


class Sonar:
#TODO implement scanning space in front of robot
    def __init__(self):
        self.array = [0, 0, 0]
        self.segments = 5
        self.view_angle = 110

    def thread_distance_values(self):
        #TODO read angle of motor and set value in array
        while True:
            if self.array[0] > 80:
                self.array[0] = 0
            if self.array[1] > 80:
                self.array[1] = 0
            if self.array[2] > 80:
                self.array[2] = 0

            self.array[0] = self.array[0] + 1
            self.array[1] = self.array[1] + 2
            self.array[2] = self.array[2] + 3
            sleep(1)

    def thread_motor_rotation(self):
        pass
        #TODO rotate motor

    def run(self):
        t1 = Thread(target=self.thread_distance_values)
        t1.setDaemon(True)
        t1.start()

    def get_distance(self):
        return self.array

    def get_segments(self):
        return self.segments

    def get_view_angle(self):
        return self.view_angle

    def callback_after_corner(self, callback):
        pass
        #TODO call this callback after full rotation from one side
