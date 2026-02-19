from pudu_ui.navigation import Navigator
from pudu_ui import App


from constants import MENU, SCREEN_HEIGHT, SCREEN_WIDTH
from controllers import MenuController, PlayController


APP_NAME = "Line Game"


class GameApp(App):
    def __init__(self):
        super().__init__(
            width=SCREEN_WIDTH, height=SCREEN_HEIGHT, caption=APP_NAME
        )
        self.navigator = Navigator()
        menu_controller = MenuController(self, self.navigator)
        self.navigator.add_controller(menu_controller)
        play_controller = PlayController(self, self.navigator)
        self.navigator.add_controller(play_controller)
        self.navigator.change(MENU)

    def update(self, dt):
        controller = self.navigator.current_controller
        if (
            controller and hasattr(controller, 'update')
        ):
            controller.update(dt)
        super().update(dt)
