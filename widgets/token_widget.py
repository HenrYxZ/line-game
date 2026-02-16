from dataclasses import dataclass, field
from pudu_ui import Frame, FrameParams, Params
from pudu_ui.colors import Color
from pudu_ui.styles.frames import FrameStyle
import pudu_ui
from pyglet.graphics import Batch


def default_token_color():
    return pudu_ui.colors.GRAY


@dataclass
class TokenWidgetParams(Params):
    color: Color = field(default_factory=default_token_color)


class TokenWidget(Frame):
    def __init__(self, params: TokenWidgetParams, batch: Batch):
        frame_style = FrameStyle()
        frame_style.set_solid_color(params.color)
        frame_params = FrameParams(
            x=params.x, y=params.y, width=params.width, height=params.height,
            focusable=params.focusable,
            debug_label_color=params.debug_label_color,
            style=frame_style
        )
        super().__init__(params=frame_params, batch=batch)
