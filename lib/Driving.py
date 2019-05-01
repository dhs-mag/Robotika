from ev3dev2.motor import MoveSteering
from ev3dev2.motor import MoveTank
from ev3dev2.motor import SpeedPercent
from ev3dev2.motor import OUTPUT_A, OUTPUT_B

class Driving:

    def __init__(self):
        self.tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

    def forward(self):
        self.tank_drive.on_for_seconds(20, 20, 1)

    def left(self):
        self.tank_drive.on_for_seconds(20, 5, 0.5)

    def left_rotate(self):
        self.tank_drive.on_for_seconds(10, -10, 1.0)

    def back(self):
        self.tank_drive.on_for_seconds(-20, -20, 1)

    def right(self):
        self.tank_drive.on_for_seconds(5, 20, 0.5)

    def right_rotate(self):
        self.tank_drive.on_for_seconds(-10, 10, 1.0)

    def back_rotate(self):
        self.tank_drive.on_for_seconds(-10, 10, 2.5)
