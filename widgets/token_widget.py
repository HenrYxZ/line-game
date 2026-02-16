from pudu_ui import Frame, FrameParams
from pudu_ui.colors import Color
from pudu_ui.styles.frames import FrameStyle
import pudu_ui
from pyglet.graphics import Batch


DEFAULT_TOKEN_COLOR = pudu_ui.colors.GRAY
TOKEN_BORDER_WIDTH = 3
TOKEN_BORDER_RADIUS = 12


class TokenWidget(Frame):
    def __init__(
        self, color: Color = DEFAULT_TOKEN_COLOR,
        batch: Batch | None = None
    ):
        frame_style = FrameStyle()
        frame_style.set_solid_color(color)
        frame_style.set_uniform_radius(TOKEN_BORDER_RADIUS)
        frame_style.border_width = TOKEN_BORDER_WIDTH
        frame_params = FrameParams(style=frame_style)
        super().__init__(params=frame_params, batch=batch)
