#!usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from time import sleep

# lm = LargeMotor()
sm = MediumMotor(OUTPUT_C)
dis = InfraredSensor()
viewAngle = 120
viewSectors = 5

arraySectorDistance = [0, 0, 0, 0, 0]


#set corner
sm.on_for_degrees(speed=5, degrees=viewAngle/2)
sm.on_for_degrees(speed=5, degrees=-viewAngle/(viewSectors*2))


for i in range(10):

    print("Iteration", i + 1)
    for iLeft in range(5):
        # TODO add sleep?
        arraySectorDistance[iLeft] = dis.value()
        sm.on_for_degrees(speed=5, degrees=-viewAngle / viewSectors)
    print("After left", arraySectorDistance)

    for iRight in range(5):
        #TODO add sleep?
        arraySectorDistance[4 - iRight] = dis.value()
        sm.on_for_degrees(speed=5, degrees=viewAngle / viewSectors)
    print("After right", arraySectorDistance)


sm.on_for_degrees(speed=5, degrees=-viewAngle/2)
sm.on_for_degrees(speed=5, degrees=viewAngle/(viewSectors*2))



# '''
# This will run the large motor at 50% of its
# rated maximum speed of 1050 deg/s.
# 50% x 1050 = 525 deg/s
# '''
# lm.on_for_seconds(speed = 50, seconds=3)
# sleep(1)
#
# '''
# speed and seconds are both POSITIONAL
# arguments which means
# you don't have to include the parameter names as
# long as you put the arguments in this order
# (speed then seconds) so this is the same as
# the previous command:
# '''
# lm.on_for_seconds(50, 3)
# sleep(1)
#
# '''
# This will run at 500 degrees per second (DPS).
# You should be able to hear that the motor runs a
# little slower than before.
# '''
# lm.on_for_seconds(speed=SpeedDPS(500), seconds=3)
# sleep(1)
#
# # 36000 degrees per minute (DPM) (rarely useful!)
# lm.on_for_seconds(speed=SpeedDPM(36000), seconds=3)
# sleep(1)
#
# # 2 rotations per second (RPS)
# lm.on_for_seconds(speed=SpeedRPS(2), seconds=3)
# sleep(1)
#
# # 100 rotations per minute(RPM)
# lm.on_for_seconds(speed=SpeedRPM(100), seconds=3)