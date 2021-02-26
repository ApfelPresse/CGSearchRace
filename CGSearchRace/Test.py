import time
import unittest
from math import sqrt

from CGSearchRace.Constants import Constants
from CGSearchRace.Referee import Referee
from CGSearchRace.Tracks import tracks


class Test(unittest.TestCase):

    def test_simulation(self):
        checksum_expected = 253300258.23805723
        checksum = 0

        start = time.time()

        for track in tracks:
            ref = Referee(track)
            for i in range(Constants.MAX_TIME):
                current_checkpoint = ref.game.get_next_checkpoint_id()
                check_x = ref.game.checkpoints[current_checkpoint].x
                check_y = ref.game.checkpoints[current_checkpoint].y

                checksum += sqrt((check_x ** 2 + check_y ** 2))

                ref.game.input = f"{check_x} {check_y} 100"
                ref.game_turn()

                if ref.game.isDone:
                    break

        end = time.time() - start
        print(f"Execution time {end}")
        diff = abs(checksum - checksum_expected)
        print(f"Diff checksum {diff}")
        assert diff == 0


if __name__ == '__main__':
    unittest.main()
