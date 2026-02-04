from pudu_ui import Label, LabelParams
from pudu_ui.colors import WHITE
from pudu_ui.styles.fonts import FontStyle
from pyglet.graphics import Batch


FONT_SIZE = 28


class InfoLabel(Label):
    def __init__(self, x: float, y: float, text: str, batch: Batch):
        style = FontStyle(color=WHITE)
        label_params = LabelParams(
            x=x, y=y, text=text, anchor_x='center', anchor_y='center',
            style=style
        )
        super().__init__(params=label_params, batch=batch)
