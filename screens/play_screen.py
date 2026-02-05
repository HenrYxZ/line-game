from pudu_ui import Screen


from constants import SCREEN_HEIGHT
from game import get_random_tokens, Game
from widgets import InfoLabel


def format_time(time: float) -> str:
    minutes, seconds = divmod(time, 60)
    return "%02d:%02d" % (minutes, seconds)


class PlayScreen(Screen):
    def __init__(self, player_name: str):
        super().__init__('PlayScreen')
        # Init Game
        tokens = get_random_tokens()
        original_tokens = get_random_tokens()
        start_time = 0.0
        self.game = Game(tokens, original_tokens, start_time, player_name)
        if self.game.is_solved():
            # ensure game is not solved
            self.game.swap(0, 9)

        # Init UI
        time_label_x = 250
        time_label_y = SCREEN_HEIGHT - 50
        self.time_label = InfoLabel(
            x=time_label_x, y=time_label_y, text=format_time(self.game.time),
            batch=self.batch
        )
