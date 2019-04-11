from time import sleep
from threading import Thread


class Sonar:

    def __init__(self):
        self.array = [0, 0, 0]

    def thread_distance_values(self):
        #TODO read angle of motor and set value in array
        while True:
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

    def callback_after_corner(self, callback):
        pass
        #TODO call this callback after full rotation from one side
