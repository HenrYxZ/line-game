from pudu_ui.layouts import ListLayout, ListLayoutParams
from pyglet.event import EVENT_HANDLED, EVENT_HANDLE_STATE, EVENT_UNHANDLED
from pyglet.graphics import Batch
from pyglet.window import key
from typing import Callable


from constants import SCREEN_WIDTH, SCREEN_HEIGHT


INTER_ITEM_SPACING = 10
LIST_HEIGHT = 100
NUM_TOKENS = 10
LIST_WIDTH = NUM_TOKENS * LIST_HEIGHT + 9 * INTER_ITEM_SPACING
LIST_X = SCREEN_WIDTH / 2 - LIST_WIDTH / 2
LIST_Y = SCREEN_HEIGHT / 2 - LIST_HEIGHT / 2


class TokenList(ListLayout):
    def __init__(
        self,
        on_select_callback: Callable[[int], None] = lambda: None,
        batch: Batch | None = None
    ):
        params = ListLayoutParams(
            x=LIST_X, y=LIST_Y, width=LIST_WIDTH, height=LIST_HEIGHT,
            inter_item_spacing=INTER_ITEM_SPACING
        )
        super().__init__(params, batch=batch)
        self.on_select_callback = on_select_callback

    def on_key_press(self, symbol, _) -> EVENT_HANDLE_STATE:
        if super().on_key_press(symbol, _) == EVENT_UNHANDLED:
            if (
                symbol == key.ENTER or
                symbol == key.RETURN or
                symbol == key.SPACE
            ):
                self.on_select(self.current_item)
                return EVENT_HANDLED
        return EVENT_UNHANDLED

    def on_select(self, idx: int):
        item = self.get_current_item()
        if item:
            item.unfocus()
            item.select()
            self.on_select_callback(idx)
