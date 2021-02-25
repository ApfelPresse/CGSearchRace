from math import degrees

from Car import Car
from Checkpoint import Checkpoint
from Constants import Constants


class Game:
    def __init__(self, user_input):
        self.isDone = None
        self.checkpoints = []
        for check in user_input.split(";"):
            split = check.split(" ")
            self.checkpoints.append(Checkpoint(int(split[0]), int(split[1])))

        self.car = Car(self.checkpoints[0].x, self.checkpoints[0].y, 0)
        self.car.angle = self.car.prev_angle = self.car.get_angle(self.checkpoints[1])
        self.car.adjust()

        self.currentCheckpoint = 0
        self.colTime = 0.0

        self.timer = 0

        self.manager = None
        self.totalCheckpoints = len(self.checkpoints) * Constants.Laps

        self.input = "X Y THRUST"

    def on_round(self):
        if self.isDone:
            return

        self.car.handle_input_(self.input)
        self.check_collisions()
        self.car.adjust()

        if not self.isDone:
            self.timer += 1

        if self.timer == Constants.MAX_TIME and not self.isDone:
            self.isDone = True

    def check_collisions(self):
        has_collided = True
        t = 0.0
        self.colTime = 2.0
        while not self.isDone and has_collided:
            has_collided = False
            col = self.car.get_collision(self.get_next_checkpoint(), Constants.CheckpointRadius)
            if col.time >= 0.0 and col.time + t <= 1.0:
                has_collided = True
                self.currentCheckpoint += 1
                t += col.time
                self.colTime = t
                self.car.move(col.time)
                if self.currentCheckpoint >= self.totalCheckpoints:
                    self.isDone = True
        self.car.move(1.0 - t)

    def get_initial_data(self):
        data = [self.totalCheckpoints]
        current = 1
        for i in range(self.totalCheckpoints):
            check = self.checkpoints[(current + 1) % len(self.checkpoints)]
            data.append(f"{check.x} {check.y}")
            current += 1
        return data

    def get_data(self):
        data = []
        angle = round(degrees(self.car.angle))
        inputs = [self.currentCheckpoint, self.car.x, self.car.y, self.car.vx, self.car.vy, angle]
        formatted_input = f"{inputs}".replace(", ", " ").replace("[", "").replace("]", "")

        data.append(formatted_input)
        return data

    def get_next_checkpoint(self):
        return self.checkpoints[self.get_next_checkpoint_id()]

    def get_next_checkpoint_id(self, pl=1):
        return (self.currentCheckpoint + pl) % len(self.checkpoints)
