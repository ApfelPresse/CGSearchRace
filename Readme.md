# Port [CGSearchRace](https://github.com/Illedan/CGSearchRace) to Python

## Install
    pip install git+https://github.com/ApfelPresse/CGSearchRace.git#egg=CGSearchRace
    
## Use

```python
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
```

## Plot Race

```python
import imageio
import matplotlib.pyplot as plt
import numpy as np

from CGSearchRace.Constants import Constants
from CGSearchRace.Referee import Referee
from CGSearchRace.Tracks import tracks


def convert_to_gif(name: str, frames: list):
    imageio.mimsave(f'./{name}.gif', frames, fps=5)


def plot_current_frame(checkpoints, current, car):
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_xlim((0, 16000))
    ax.set_ylim((0, 9000))

    for j, checkpoint in enumerate(checkpoints):
        color = "b" if j == current else "r"
        ax.add_patch(plt.Circle((checkpoint.x, checkpoint.y), 400, color=color))

    ax.add_patch(plt.Circle((car.x, car.y), 300, color='g'))

    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    plt.close()
    return image


if __name__ == '__main__':
    for track_i, track in enumerate(tracks):
        ref = Referee(track)

        images = []

        for i in range(Constants.MAX_TIME):
            current_checkpoint = ref.game.get_next_checkpoint_id()
            check_x = ref.game.checkpoints[current_checkpoint].x
            check_y = ref.game.checkpoints[current_checkpoint].y

            ref.game.input = f"{check_x} {check_y} 100"
            ref.game_turn()

            if i % 2 == 0:
                images.append(plot_current_frame(ref.game.checkpoints, ref.game.get_next_checkpoint_id(), ref.game.car))

            if ref.game.isDone:
                break

        convert_to_gif(f"track_{track_i}", images)

        print(f"Track {track_i} done!")
```

![Example](track_example.gif)