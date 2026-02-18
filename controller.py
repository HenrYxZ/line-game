from pudu_ui import App, Controller


from controllers import PlayController

class GameController(Controller):
    def __init__(self, app: App):
        super().__init__(app, 'GameController')
        self.current_controller = None
        self.play()

    def play(self):
        self.current_controller = PlayController(app=self.app)

    def update(self, dt: float):
        self.current_controller.update(dt)
