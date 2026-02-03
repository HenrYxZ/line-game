from dataclasses import dataclass
from pudu_ui.colors import (
    Color,
    ORANGE, RED, YELLOW, GREEN, BLUE_GREEN, BLUE, PURPLE, VIOLET, BLACK, WHITE
)
import random


NUM_TOKENS = 10


@dataclass
class Token:
    color: Color

    def __eq__(self, other) -> bool:
        if isinstance(other, Token):
            return self.color.as_tuple() == other.color.as_tuple()
        return False



@dataclass
class Game:
    tokens: list[Token]
    original_tokens: list[Token]
    time: float
    player_name: str

    def is_solved(self):
        n = len(self.tokens)
        for i in range(n):
            if (
                self.tokens[i].color.as_vec3() !=
                self.original_tokens[i].color.as_vec3()
            ):
                return False
        return True

    def swap(self, i: int, j: int):
        temp = self.tokens[i]
        self.tokens[i] = self.tokens[j]
        self.tokens[j] = temp


def get_colors() -> list[Color]:
    return [
        ORANGE, RED, YELLOW, GREEN, BLUE_GREEN, BLUE, PURPLE, VIOLET, BLACK,
        WHITE
    ]


def get_random_tokens() -> list[Token]:
    colors = get_colors()
    tokens = [Token(color) for color in colors]
    random.shuffle(tokens)
    return tokens
