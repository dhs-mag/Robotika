import math
from time import sleep
from threading import Thread
from ev3dev2.motor import OUTPUT_C
from ev3dev2.motor import MediumMotor
from ev3dev2.sensor.lego import InfraredSensor


class Sonar:
#TODO implement scanning space in front of robot
    def __init__(self):
        self.tempDistance = []
        self.actualSector = 0
        self.speed = 5
        self.segments = 5
        self.distanceSegments = [0] * self.segments
        self.view_angle = 110
        self.Motor = MediumMotor(OUTPUT_C)
        self.ISensor = InfraredSensor()

    def thread_distance_values(self):
        while True:
            print(self.Motor.position)  # TODO check if is this correct degrees

            # sector = math.floor(self.Motor.position + (self.view_angle / 2) / (self.view_angle / self.segments))
            #
            # if sector != self.actualSector:
            #     self.array[self.actualSector] = math.fsum(self.tempDistance) / len(self.tempDistance)
            #     self.tempDistance = []
            #     self.actualSector = sector
            #
            # self.tempDistance.append(self.ISensor.value())
            # sleep(0.1)

    def thread_motor_rotation(self):
        self.Motor.on_for_degrees(speed=self.speed, degrees=-self.view_angle / self.segments)
        while True:
            self.Motor.on_for_degrees(speed=self.speed, degrees=self.view_angle)
            self.Motor.on_for_degrees(speed=self.speed, degrees=-self.view_angle)

    def run(self):
        t1 = Thread(target=self.thread_distance_values)
        t2 = Thread(target=self.thread_motor_rotation)
        t1.setDaemon(True)
        t2.setDaemon(True)
        t1.start()
        t2.start()

    def get_distance(self):
        return self.distanceSegments

    def get_segments(self):
        return self.segments

    def get_view_angle(self):
        return self.view_angle

    def callback_after_corner(self, callback):
        pass
        #TODO call this callback after full rotation from one side
