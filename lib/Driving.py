from ev3dev2.motor import MoveTank
from ev3dev2.motor import OUTPUT_A, OUTPUT_B


class Driving:

    def __init__(self):
        self.tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
        self.speed = 40
        self.status = "none"

    def __del__(self):
        self.tank_drive.off()

    def stop(self):
        if self.tank_drive.is_running:
            self.tank_drive.off()

    def forward(self):
        if self.status is not "forward":
            self.stop()
        self.tank_drive.on(self.speed, self.speed)
        self.status = "forward"

    def left(self):
        if self.status is not "left":
            self.stop()
        self.tank_drive.on(self.speed * 1.5, self.speed / 2)
        self.status = "left"

    def left_rotate(self):
        if self.status is not "left_rotate":
            self.stop()
        self.tank_drive.on(self.speed, -self.speed)
        self.status = "left_rotate"

    def back(self):
        if self.status is not "back":
            self.stop()
        self.tank_drive.on(-self.speed, -self.speed)
        self.status = "back"

    def right(self):
        if self.status is not "right":
            self.stop()
        self.tank_drive.on(self.speed / 2, self.speed * 1.5)
        self.status = "right"

    def right_rotate(self):
        if self.status is not "right_rotate":
            self.stop()
        self.tank_drive.on(-self.speed, self.speed)
        self.status = "right_rotate"
