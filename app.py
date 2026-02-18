from pudu_ui import App


from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from controller import GameController


APP_NAME = "Line Game"


class GameApp(App):
    def __init__(self):
        super().__init__(
            width=SCREEN_WIDTH, height=SCREEN_HEIGHT, caption=APP_NAME
        )
        self.controller = GameController(self)

    def update(self, dt):
        self.controller.update(dt)
        super().update(dt)