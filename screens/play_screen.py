from pudu_ui import Screen


from constants import SCREEN_HEIGHT, SCREEN_WIDTH
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
        labels_y = SCREEN_HEIGHT - 50
        time_label_x = 250
        self.time_label = InfoLabel(
            x=time_label_x, y=labels_y, text=format_time(self.game.time),
            batch=self.batch
        )

        name_label_x = SCREEN_WIDTH / 2
        self.name_label = InfoLabel(
            x=name_label_x, y=labels_y, text=player_name,
            batch=self.batch
        )

        count = self.game.get_count()
        done_label_x = SCREEN_WIDTH - time_label_x
        self.done_label = InfoLabel(
            x=done_label_x, y=labels_y, text=f"{count}/{len(self.game.tokens)}",
            batch=self.batch
        )
