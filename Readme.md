# Port [CGSearchRace](https://github.com/Illedan/CGSearchRace) to Python

## Install
    pip install git+https://github.com/ApfelPresse/CGSearchRace.git#egg=CGSearchRace
    
## Use

    from CGSearchRace.Constants import Constants
    from CGSearchRace.Referee import Referee
    from CGSearchRace.Tracks import tracks
    
    if __name__ == '__main__':
        for track_i, track in enumerate(tracks):
            ref = Referee(track)
    
            for i in range(Constants.MAX_TIME):
                current_checkpoint = ref.game.get_next_checkpoint_id()
                check_x = ref.game.checkpoints[current_checkpoint].x
                check_y = ref.game.checkpoints[current_checkpoint].y
    
                ref.game.input = f"{check_x} {check_y} 100"
                ref.game_turn()
    
                if ref.game.isDone:
                    break
            print(f"Track {track_i} done!")

![Example](track_example.gif)