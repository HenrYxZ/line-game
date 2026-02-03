import unittest


from game import Game, get_random_tokens


def create_random_game() -> Game:
    original_tokens = get_random_tokens()
    tokens = [
        t for t in original_tokens
    ]
    time = 15 * 60 + 2.32
    game = Game(tokens, original_tokens, time, 'test player')
    return game


class GameTestCase(unittest.TestCase):
    def test_swap(self):
        game = create_random_game()
        i, j = 4, 6
        value_i = game.tokens[i]
        value_j = game.tokens[j]
        game.swap(i, j)
        self.assertEqual(game.tokens[i], value_j)
        self.assertEqual(game.tokens[j], value_i)


    def test_solved(self):
        game = create_random_game()
        game.swap(3, 5)
        game.swap(5, 9)
        self.assertEqual(game.is_solved(), False)
        game.swap(5, 9)
        self.assertEqual(game.is_solved(), False)
        game.swap(5, 3)
        self.assertEqual(game.is_solved(), True)


if __name__ == '__main__':
    unittest.main()
