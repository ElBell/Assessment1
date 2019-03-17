from enum import Enum


class RPS(Enum):
    ROCK = {"winner": "paper", "loser": "scissors"}
    PAPER = {"winner": "scissors", "loser": "rock"}
    SCISSORS = {"winner": "rock", "loser": "paper"}


class RPSEvaluator:

    @staticmethod
    def get_winning_move(move: str) -> str:
        return RPS[move.upper()].value.get("winner")

    @staticmethod
    def get_losing_move(move: str) -> str:
        return RPS[move.upper()].value.get("loser")

    @staticmethod
    def get_winner(move1: str, move2: str) -> str:
        return move1 if RPSEvaluator.get_losing_move(move1) == move2 else move2
