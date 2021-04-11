from enum import Enum


class GameBoard(Enum):
    EASY = 0
    MED = 1
    HARD = 2


class Field(Enum):
    EMPTY = 0
    WALL = 1
    CHEST = 2
    PLAYER = 3
    GOAL = 4


class Direction(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3
