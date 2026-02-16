from pudu_ui import App


from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from controller import GameController


APP_NAME = "Line Game"



app = App(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, caption=APP_NAME)
controller = GameController(app)


if __name__ == '__main__':
    app.run()
