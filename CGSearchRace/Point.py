from math import sqrt, atan2

from CGSearchRace.Constants import Constants


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return sqrt((self.x - p.x) * (self.x - p.x) + (self.y - p.y) * (self.y - p.y))

    def get_angle(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return atan2(dy, dx)

    def move_to(self, p, distance):
        d = self.distance(p)

        if d < Constants.EPSILON:
            return

        dx = p.x - self.x
        dy = p.y - self.y
        coefficient = distance / d

        self.x += dx * coefficient
        self.y += dy * coefficient

    def get_point(self, target, distance):
        d = self.distance(target)

        if d < Constants.EPSILON:
            return target.clone_point()

        dx = target.x - self.x
        dy = target.y - self.y
        coefficient = distance / d

        x = self.x + dx * coefficient
        y = self.y + dy * coefficient
        return Point(x, y)

    def is_in_range(self, p, rang):
        return p != self and self.distance(p) <= rang

    def clone_point(self):
        return Point(self.x, self.y)
