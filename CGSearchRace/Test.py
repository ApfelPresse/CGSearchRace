import unittest

import numpy as np

from CGSearchRace.Constants import Constants
from CGSearchRace.Referee import Referee
from CGSearchRace.Tracks import tracks


class Test(unittest.TestCase):

    def test_simulation(self):
        points_from_coding_games = [[10353, 1986], [10258, 2019], [10083, 2080], [9840, 2165], [9540, 2270],
                                    [9191, 2392], [8800, 2528], [8374, 2676], [7918, 2835], [7436, 3003], [6932, 3179],
                                    [6410, 3361], [5872, 3549], [5321, 3742], [4759, 3939], [4188, 4140], [3609, 4345],
                                    [3024, 4553], [2427, 4733], [1823, 4858], [1228, 4908], [661, 4871], [145, 4746],
                                    [-295, 4540], [-641, 4268], [-879, 3955], [-1002, 3628], [-1012, 3316],
                                    [-920, 3041], [-743, 2803], [-493, 2601], [-181, 2437], [183, 2309], [590, 2217],
                                    [1033, 2161], [1506, 2142], [2001, 2162], [2511, 2223], [3024, 2333], [3518, 2507],
                                    [4018, 2713], [4538, 2918], [5080, 3093], [5637, 3220], [6207, 3302], [6787, 3341],
                                    [7373, 3338], [7962, 3294], [8549, 3210], [9130, 3082], [9698, 2907], [10238, 2677],
                                    [10726, 2386]]

        car_pos = []
        for track in tracks[:1]:
            ref = Referee(track)
            for i in range(Constants.MAX_TIME):
                current_checkpoint = ref.game.get_next_checkpoint_id()
                check_x = ref.game.checkpoints[current_checkpoint].x
                check_y = ref.game.checkpoints[current_checkpoint].y

                if i == 53:
                    break

                car_pos.append([int(ref.game.car.x), int(ref.game.car.y)])

                ref.game.input = f"{check_x} {check_y} 100"
                ref.game_turn()

                if ref.game.isDone:
                    break

        sum_coding_games = np.sum(points_from_coding_games)
        sum_local_game = np.sum(car_pos)
        assert abs(sum_coding_games - sum_local_game) < 100


if __name__ == '__main__':
    unittest.main()
