#!usr/bin/env python3

import math
from time import sleep
from threading import Thread
from ev3dev2.motor import OUTPUT_C
from ev3dev2.motor import MediumMotor
from ev3dev2.motor import SpeedPercent
from ev3dev2.sensor.lego import InfraredSensor


class Sonar:

    def __init__(self):
        self.tempDistance = []
        self.actualSector = 0
        self.speed = SpeedPercent(20)
        self.segments = 7
        self.distanceSegments = [0] * self.segments
        self.view_angle = 140
        self.Motor = MediumMotor(OUTPUT_C)
        self.Motor.reset()
        self.ISensor = InfraredSensor()
        self.callback = None

    def thread_distance_values(self):
        while True:
            sector = math.floor((self.Motor.position - (self.view_angle / 2)) / (self.view_angle / self.segments)) * -1
            sector = sector - 1
            self.tempDistance.append(self.ISensor.value())

            if sector < 0:
                sector = 0

            if sector >= self.segments:
                sector = self.segments - 1

            if sector != self.actualSector:
                self.distanceSegments[self.actualSector] = math.fsum(self.tempDistance) / len(self.tempDistance)
                self.tempDistance = []
                self.actualSector = sector
                if self.actualSector is 0 or self.actualSector is self.segments - 1:
                    if self.callback is not None:
                        self.callback()

            sleep(0.01)

    def thread_motor_rotation(self):
        self.Motor.on_for_degrees(speed=self.speed, degrees=-self.view_angle / 2)
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

    def set_callback(self, callback):
        self.callback = callback

    def get_distance(self):
        return self.distanceSegments

    def get_segments(self):
        return self.segments

    def get_view_angle(self):
        return self.view_angle

    def get_nav_array(self):
        print('distances', self.distanceSegments)
        segment = math.floor(self.segments / 3)
        segment_two = math.floor((self.segments / 3) * 2)
        nav_array = [
            math.fsum(self.distanceSegments[0:segment])/segment,
            math.fsum(self.distanceSegments[segment:segment_two+1])/(segment_two-segment),
            math.fsum(self.distanceSegments[segment_two+1:])/segment,
        ]
        print('nav_array = ', nav_array)
        return nav_array