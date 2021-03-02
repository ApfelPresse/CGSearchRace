from math import cos, sin, radians, degrees, copysign

from CGSearchRace.Constants import Constants
from CGSearchRace.Point import Point
from CGSearchRace.Unit import Unit


class Car(Unit):

    def __init__(self, x, y, angle):
        super().__init__(x, y)
        self.angle = angle
        self.friction = Constants.CAR_FRICTION
        self.thrust = 0
        self.prev_angle = 0
        self.target = None
        self.debug = False

    def handle_input_(self, user_input):
        self.prev_angle = self.angle
        self.target = None
        split = user_input.split(" ")

        if split[0] == "EXPERT":
            try:
                angle = int(split[1])
                thrust = int(split[2])
            except Exception:
                raise Exception("Can't parse expert input integers. ")

            if thrust < 0 or thrust > Constants.CAR_MAX_THRUST:
                raise Exception("Invalid thrust")

            if angle < -18 or angle > 18:
                raise Exception("Invalid angle")

            self.handle_expert_input(angle, thrust)
            if split.length > 3:
                total_length = len(f"EXPERT :angle :thrust")
                self.message = user_input.substring(total_length)
            else:
                self.message = ""
        else:
            try:
                x = int(split[0])
                y = int(split[1])
                self.target = Point(x, y)
                thrust = int(split[2])
            except Exception:
                raise Exception("Can't parse action. Has to be X Y THRUST.")

            if thrust < 0 or thrust > Constants.CAR_MAX_THRUST:
                raise Exception("Invalid thrust")

            self.handle_input(x, y, thrust)
            if len(split) > 3:
                total_length = len(f":x :y :thrust")
                self.message = user_input.substring(total_length)
            else:
                self.message = ""

        if "debug" in self.message:
            self.debug = True

    def handle_expert_input(self, angle: int, thrust: int):
        new_angle = degrees(self.angle) + angle
        self.angle = radians(new_angle)
        self.thrust_towards_heading(thrust)

    def handle_input(self, x: int, y: int, thrust: int):
        if self.x != x or self.y != y:
            angle = self.get_angle(Point(x, y))
            relative_angle = self.short_angle_dist(self.angle, angle)
            if abs(relative_angle) >= Constants.MAX_ROTATION_PER_TURN:
                angle = self.angle + Constants.MAX_ROTATION_PER_TURN * copysign(1, relative_angle)

            self.angle = angle
            self.thrust_towards_heading(thrust)

    def thrust_towards_heading(self, thrust: int):
        vx = cos(self.angle) * thrust
        vy = sin(self.angle) * thrust
        self.vx += vx
        self.vy += vy

    def adjust(self):
        super().adjust()
        self.angle = radians(round(degrees(self.angle)))
        self.angle = self.angle % (Constants.PI * 2)

    def short_angle_dist(self, a0: float, a1: float):
        max_angle = Constants.PI * 2
        da = (a1 - a0) % max_angle
        return 2 * da % max_angle - da
