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
        self.selected_token_idx = -1
        self.game = Game(tokens, original_tokens, start_time, player_name)
        if self.game.is_solved():
            # ensure game is not solved
            self.game.swap(0, 9)

        self.screen = PlayScreen(game=self.game, player_name=player_name)
        self.app.set_screen(self.screen)

    def update(self, dt: float):
        if self.game.is_solved():
            print("You win!")

        self.game.time += dt
        self.screen.time_label.text = format_time(self.game.time)
        self.screen.time_label.invalidate()

    def on_select_token(self, idx: int):
        if self.selected_token_idx:
            # Swap tokens
            i = self.selected_token_idx
            j = idx
            self.game.swap(i, j)

            list_layout = self.screen.token_listlayout
            temp = list_layout[i]
            list_layout[i] = list_layout[j]
            list_layout[j] = temp
            list_layout.invalidate()
            self.selected_token_idx = -1

            # Check new score
            score = self.game.get_count()
            total = len(self.game.tokens)
            # There could be a better way of updating UI from changes in the
            # model, for now it's all manual
            self.screen.done_label.text = f"{score}/{total}"
            self.screen.done_label.invalidate()
        else:
            # Store currently selected token
            self.selected_token_idx = idx
