from pudu_ui import App


from controller import GameController


APP_NAME = "Line Game"



# app = App(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, caption=APP_NAME)
app = App(caption=APP_NAME)
controller = GameController(app)


if __name__ == '__main__':
    print(app.width, app.height)
    app.run()
