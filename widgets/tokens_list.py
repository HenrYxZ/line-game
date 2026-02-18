from pudu_ui.layouts import ListLayout, ListLayoutParams
from pyglet.graphics import Batch


from constants import SCREEN_WIDTH, SCREEN_HEIGHT


INTER_ITEM_SPACING = 10
LIST_HEIGHT = 100
NUM_TOKENS = 10
LIST_WIDTH = NUM_TOKENS * LIST_HEIGHT + 9 * INTER_ITEM_SPACING
LIST_X = SCREEN_WIDTH / 2 - LIST_WIDTH / 2
LIST_Y = SCREEN_HEIGHT / 2 - LIST_HEIGHT / 2


class TokenList(ListLayout):
    def __init__(self, batch: Batch | None = None):
        params = ListLayoutParams(
            x=LIST_X, y=LIST_Y, width=LIST_WIDTH, height=LIST_HEIGHT,
            inter_item_spacing=INTER_ITEM_SPACING
        )
        super().__init__(params, batch=batch)
