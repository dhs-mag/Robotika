#!usr/bin/env python3
# from ev3dev2.motor import *
# from ev3dev2.sensor.lego import *
from time import sleep

from lib.Driving import Driving
from lib.Navigator import Navigator
from lib.Sonar import Sonar
from lib.Server import Server
#
# # lm = LargeMotor()
# sm = MediumMotor(OUTPUT_C)
# dis = InfraredSensor()
# viewAngle = 120
# viewSectors = 5
#
# arraySectorDistance = [0, 0, 0, 0, 0]
#
#
# #set corner
# sm.on_for_degrees(speed=5, degrees=viewAngle/2)
# sm.on_for_degrees(speed=5, degrees=-viewAngle/(viewSectors*2))
#
#
# for i in range(10):
#
#     print("Iteration", i + 1)
#     for iLeft in range(5):
#         # TODO add sleep?
#         arraySectorDistance[iLeft] = dis.value()
#         sm.on_for_degrees(speed=5, degrees=-viewAngle / viewSectors)
#     print("After left", arraySectorDistance)
#
#     for iRight in range(5):
#         #TODO add sleep?
#         arraySectorDistance[4 - iRight] = dis.value()
#         sm.on_for_degrees(speed=5, degrees=viewAngle / viewSectors)
#     print("After right", arraySectorDistance)
#
#
# sm.on_for_degrees(speed=5, degrees=-viewAngle/2)
# sm.on_for_degrees(speed=5, degrees=viewAngle/(viewSectors*2))
from threading import Thread

# array = [0, 0, 0]
#
#
# def i_run_on_background():
#     while True:
#         array[0] = array[0] + 1
#         array[1] = array[1] + 2
#         array[2] = array[2] + 3
#         sleep(1)
#
#
# t = Thread(target=i_run_on_background)
# t.setDaemon(True)
# t.start()

dis = Sonar()
motor = Driving()
server = Server(8081)
nav = Navigator()

dis.run()

nav.set_sonar(dis)
nav.set_driving(motor)
nav.run()
dis.set_callback(nav.set_running)

server.set_sonar(dis)
server.set_driving(motor)
server.run()

#while True:
#    print(dis.get_distance())
