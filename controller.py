from pudu_ui import App, Controller


from screens import PlayScreen


class GameController(Controller):
    def __init__(self, app: App):
        super().__init__(app, 'GameController')
        self.play('Player Name')

    def play(self, player_name: str):
        play_screen = PlayScreen(player_name=player_name)
        self.app.set_screen(play_screen)
