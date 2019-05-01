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
        self.speed = SpeedPercent(30)
        self.segments = 7
        self.distanceSegments = [0] * self.segments
        # self.distanceSegmentsOld = [0] * self.segments
        self.view_angle = 140
        self.Motor = MediumMotor(OUTPUT_C)
        self.Motor.reset()
        self.ISensor = InfraredSensor()
        self.callback = None
        self.is_running = True

    def __del__(self):
        self.is_running = False
        self.Motor.off()
        self.Motor.on_to_position(self.speed, 0, False, False)

    def thread_distance_values(self):
        while self.is_running:
            sector = math.floor((self.Motor.position - (self.view_angle / 2)) / (self.view_angle / self.segments)) * -1
            sector = sector - 1
            self.tempDistance.append(self.ISensor.value())

            if sector < 0:
                sector = 0

            if sector >= self.segments:
                sector = self.segments - 1

            if sector != self.actualSector:

                # keep
                # nMinus2 = self.distanceSegmentsOld[self.actualSector]
                # nMinus1 = self.distanceSegments[self.actualSector]
                #
                # nRaw = mean(self.tempDistance)
                #
                # inertia = math.fabs(nMinus1 - nRaw) / 100
                #
                # n = mean([nMinus2, nMinus1, nRaw * inertia]) * 2
                # if n >= 100:
                #     n = 100
                #
                # self.distanceSegmentsOld[self.actualSector] = self.distanceSegments[self.actualSector]
                # self.distanceSegments[self.actualSector] = n

                self.distanceSegments[self.actualSector] = math.fsum(self.tempDistance) / len(self.tempDistance)
                self.tempDistance = []
                self.actualSector = sector
                if self.actualSector is 0 or self.actualSector is self.segments - 1:
                    if self.callback is not None:
                        self.callback()

            sleep(0.01)

    def thread_motor_rotation(self):
        self.Motor.on_for_degrees(speed=self.speed, degrees=-self.view_angle / 2)
        while self.is_running:
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
        # print('distances', self.distanceSegments)
        segment = math.floor(self.segments / 3)
        segment_two = math.floor((self.segments / 3) * 2)
        nav_array = [
            math.fsum(self.distanceSegments[0:segment])/segment,
            math.fsum(self.distanceSegments[segment:segment_two+1])/(segment_two-segment),
            math.fsum(self.distanceSegments[segment_two+1:])/segment,
        ]
        # print('nav_array = ', nav_array)
        return nav_array

# def mean(data):
#     """Return the sample arithmetic mean of data."""
#     n = len(data)
#     return math.fsum(data) / n
#
#
# def _ss(data):
#     """Return sum of square deviations of sequence data."""
#     c = mean(data)
#     ss = sum((x - c) ** 2 for x in data)
#     return ss
#
#
# def stddev(data, ddof=0):
#     """Calculates the population standard deviation
#     by default; specify ddof=1 to compute the sample
#     standard deviation."""
#     n = len(data)
#     ss = _ss(data)
#     pvar = ss / (n - ddof)
#     return pvar ** 0.5
