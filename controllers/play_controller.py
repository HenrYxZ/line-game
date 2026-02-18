from pudu_ui import Controller


from game import Game, get_random_tokens
from screens import PlayScreen
from utils import format_time


class PlayController(Controller):
    def on_load(self):
        super().on_load()
        # Init Game
        tokens = get_random_tokens()
        original_tokens = get_random_tokens()
        start_time = 0.0
        player_name = "Player Name"
        self.game = Game(tokens, original_tokens, start_time, player_name)
        if self.game.is_solved():
            # ensure game is not solved
            self.game.swap(0, 9)

        self.screen = PlayScreen(game=self.game, player_name=player_name)
        self.app.set_screen(self.screen)

    def update(self, dt: float):
        self.game.time += dt
        self.screen.time_label.text = format_time(self.game.time)
        self.screen.time_label.invalidate()
