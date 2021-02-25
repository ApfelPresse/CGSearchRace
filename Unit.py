from math import sqrt, atan2

from Collision import Collision
from Constants import Constants
from Point import Point


class Unit(Point):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.vx = 0.0
        self.vy = 0.0
        self.friction = 0.5

    def get_speed(self):
        return sqrt(self.vx * self.vx + self.vy * self.vy)

    def get_speed_angle(self):
        return atan2(self.vy, self.vx)

    def move(self, t):
        self.x += self.vx * t
        self.y += self.vy * t

    def adjust(self):
        self.vx = self.vx * (1.0 - self.friction)
        self.vy = self.vy * (1.0 - self.friction)

    def get_collision(self, u, checked_radius):
        if self.distance(u) <= checked_radius:
            return Collision(0.0, self, u)

        if self.vx == 0.0 and self.vy == 0.0 and u.vx == 0.0 and u.vy == 0.0:
            return Constants.NULL_COLLISION

        x2 = self.x - u.x
        y2 = self.y - u.y
        r2 = checked_radius
        vx2 = self.vx - u.vx
        vy2 = self.vy - u.vy

        a = vx2 * vx2 + vy2 * vy2

        if a <= 0.0:
            return Constants.NULL_COLLISION

        b = 2.0 * (x2 * vx2 + y2 * vy2)
        c = x2 * x2 + y2 * y2 - r2 * r2
        delta = b * b - 4.0 * a * c

        if delta < 0.0:
            return Constants.NULL_COLLISION

        t = (-b - sqrt(delta)) / (2.0 * a)

        if t <= 0.0:
            return Constants.NULL_COLLISION

        return Collision(t, self, u)
