from ev3dev2.motor import MoveSteering
from ev3dev2.motor import MoveTank
from ev3dev2.motor import SpeedPercent
from ev3dev2.motor import OUTPUT_A, OUTPUT_B

class Driving:

    def __init__(self):
        self.tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

    def forward(self):
        self.tank_drive.on_for_seconds(75, 75, 1)

    def left(self):
        self.tank_drive.on_for_seconds(75, 20, 0.5)

    def back(self):
        self.tank_drive.on_for_seconds(-75, -75, 1)

    def right(self):
        self.tank_drive.on_for_seconds(20, 75, 0.5)
