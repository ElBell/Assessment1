from unittest import TestCase

from src.main.part1.rps_evaluator import RPSEvaluator


class TestRockPaperScissorsEvaluator(TestCase):

    def test_get_winning_move(self):
        move: str = "rock"
        expected: str = "paper"
        actual: str = RPSEvaluator.get_winning_move(move)
        self.assertEqual(expected, actual)

    def test_get_losing_move(self):
        move: str = "rock"
        expected: str = "scissors"
        actual: str = RPSEvaluator.get_losing_move(move)
        self.assertEqual(expected, actual)

    def test_get_winner(self):
        move1: str = "rock"
        move2: str = "scissors"
        expected: str = "rock"
        actual: str = RPSEvaluator.get_winner(move1, move2)
        self.assertEqual(actual, expected)
