from enum import Enum

class Board():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__turn = 0
        self.__fields = [[Field.EMPTY in range(x)] in range(y)] #todo check if it works
        self.__base_fields = [[Field.EMPTY in range(x)] in range(y)]
        self.__player_pos_x = None
        self.__player_pos_y = None

    def set_field_type(self, x, y, field):
        self.__fields[x][y] = field

    def player_move(self, direction):
        if (self.check_player_collision(direction)):
            #todo

    def check_player_collision(self, direction):
        if (direction == Direction.UP and self.check_player_up_colision()):

        elif(direction == Direction.DOWN):

        elif(direction == Direction.LEFT):

        elif(direction == Direction.RIGHT):

    def check_player_up_colision(self) -> bool:
        if (self.__fields[self.__player_pos_x - 1][self.__player_pos_y] == Field.WALL):
            return False
        elif (self.__fields[self.__player_pos_x - 1][self.__player_pos_y] == Field.CHEST): #and todo sprawdzenie kolizji skrzyni):
            self.__fields[self.__player_pos_x - 2][self.__player_pos_y] = Field.CHEST
            self.__fields[self.__player_pos_x - 1][self.__player_pos_y] = self.__base_fields[self.__player_pos_x - 1][self.__player_pos_y]
        else:
            return True

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_turn(self):
        return self.__turn

    def get_board(self):
        return self.__fields


class Field(Enum):
    EMPTY = 0,
    WALL = 1,
    CHEST = 2,
    PLAYER = 3,
    GOAL = 4

class Direction(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3