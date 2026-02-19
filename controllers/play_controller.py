from pudu_ui import App, Controller


from game import Game, get_random_tokens
from screens import PlayScreen
from utils import format_time


class PlayController(Controller):
    def __init__(self, app: App, name: str):
        super().__init__(app=app, name=name)
        self.selected_token_idx = None
        self.game = None
        self.screen = None


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
        self.screen.token_listlayout.on_select_callback = self.on_select_token

    def update(self, dt: float):
        if self.game.is_solved():
            print("You win!")
            self.app.close()

        self.game.time += dt
        self.screen.time_label.text = format_time(self.game.time)
        self.screen.time_label.invalidate()

    def on_select_token(self, idx: int):
        n = len(self.game.tokens)
        if not (0 <= idx < n):
            return

        if self.selected_token_idx is not None:
            # Swap tokens
            i = self.selected_token_idx
            j = idx
            self.game.swap(i, j)

            token_widgets = self.screen.token_listlayout.children
            token_widgets[i].unselect()
            token_widgets[j].unselect()
            temp = token_widgets[i]
            token_widgets[i] = token_widgets[j]
            token_widgets[j] = temp
            self.screen.token_listlayout.invalidate()
            if self.screen.token_listlayout.is_on_focus:
                self.screen.token_listlayout.get_current_item().focus()
            self.selected_token_idx = None

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
