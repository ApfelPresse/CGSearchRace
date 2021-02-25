import numpy as np

from Collision import Collision


class Constants:
    MAX_TIME = 600
    EPSILON = 0.00001
    Laps = 3
    Width = 16000
    Height = 9000
    CheckpointRadius = 600
    PI = np.pi
    NULL_COLLISION = Collision(2.0, None, None)
    MAX_ROTATION_PER_TURN = 3.14 / 10
    CAR_MAX_THRUST = 200
    CAR_FRICTION = 0.15
