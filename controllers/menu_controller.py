from pudu_ui.navigation import Navigator
from pudu_ui import App, Button, Controller


from constants import MENU, PLAY
from screens import MenuScreen


class MenuController(Controller):
    def __init__(self, app: App, navigator: Navigator):
        super().__init__(app=app, name=MENU)
        self.navigator = navigator
        self.button_maps = [
            self.play
        ]

    def on_load(self):
        # Load screen
        self.screen = MenuScreen()
        self.app.set_screen(self.screen)

        # Set on press for buttons
        for button in self.screen.list_layout.children:
            button.on_press = self.handle_on_press

    def handle_on_press(self, button_pressed: Button):
        self.button_maps[button_pressed.index]()

    def play(self):
        self.navigator.change(PLAY)

    def update(self, dt: float):
        pass
