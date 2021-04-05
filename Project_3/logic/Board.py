from enum import Enum


class Board():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__turn = 0
        self.__fields = Field[[Field.EMPTY in range(x)] in range(y)]  # todo check if it works
        self.__base_fields = Field[[Field.EMPTY in range(x)] in range(y)]
        self.__player_pos_x = 0
        self.__player_pos_y = 0
        self.__field_under_player = 0

    def set_field_type(self, x, y, field):
        self.__fields[x][y] = field

    def player_move(self, direction):
        if direction == Direction.UP and self.check_player_up_collision():
            self.__fields[self.__player_pos_x][self.__player_pos_y] = self.__field_under_player
            self.__player_pos_x -= 1
            self.move_player()

        elif direction == Direction.DOWN and self.check_player_down_collision():
            self.__fields[self.__player_pos_x][self.__player_pos_y] = self.__field_under_player
            self.__player_pos_x += 1
            self.move_player()

        elif direction == Direction.LEFT and self.check_player_left_collision():
            self.__fields[self.__player_pos_x][self.__player_pos_y] = self.__field_under_player
            self.__player_pos_y -= 1
            self.move_player()

        elif direction == Direction.RIGHT and self.check_player_right_collision():
            self.__fields[self.__player_pos_x][self.__player_pos_y] = self.__field_under_player
            self.__player_pos_y += 1
            self.move_player()

    def move_player(self):
        self.__field_under_player = self.__fields[self.__player_pos_x][self.__player_pos_y]
        self.__fields[self.__player_pos_x][self.__player_pos_y] = Field.PLAYER

    def check_player_up_collision(self) -> bool:
        if self.get_field_based_on_player_pos(-1, 0) == Field.WALL:
            return False
        elif self.get_field_based_on_player_pos(-1, 0) == Field.CHEST and self.check_chest_collision(
                self.__player_pos_x - 2, self.__player_pos_y):
            self.__fields[self.__player_pos_x - 2][self.__player_pos_y] = Field.CHEST
            self.__fields[self.__player_pos_x - 1][self.__player_pos_y] = self.__base_fields[self.__player_pos_x - 1][
                self.__player_pos_y]
            return True
        else:
            return True

    def check_player_down_collision(self) -> bool:
        if self.get_field_based_on_player_pos(1, 0) == Field.WALL:
            return False
        elif self.get_field_based_on_player_pos(1, 0) == Field.CHEST and self.check_chest_collision(
                self.__player_pos_x + 2, self.__player_pos_y):
            self.__fields[self.__player_pos_x + 2][self.__player_pos_y] = Field.CHEST
            self.__fields[self.__player_pos_x + 1][self.__player_pos_y] = self.__base_fields[self.__player_pos_x + 1][
                self.__player_pos_y]
            return True
        else:
            return True

    def check_player_left_collision(self) -> bool:
        if self.get_field_based_on_player_pos(0, -1) == Field.WALL:
            return False
        elif self.get_field_based_on_player_pos(0, -1) == Field.CHEST and self.check_chest_collision(
                self.__player_pos_x, self.__player_pos_y - 2):
            self.__fields[self.__player_pos_x][self.__player_pos_y - 2] = Field.CHEST
            self.__fields[self.__player_pos_x][self.__player_pos_y - 1] = self.__base_fields[self.__player_pos_x][
                self.__player_pos_y - 1]
            return True
        else:
            return True

    def check_player_right_collision(self) -> bool:
        if self.get_field_based_on_player_pos(0, 1) == Field.WALL:
            return False
        elif self.get_field_based_on_player_pos(0, 1) == Field.CHEST and self.check_chest_collision(
                self.__player_pos_x, self.__player_pos_y + 2):
            self.__fields[self.__player_pos_x][self.__player_pos_y + 2] = Field.CHEST
            self.__fields[self.__player_pos_x][self.__player_pos_y + 1] = self.__base_fields[self.__player_pos_x][
                self.__player_pos_y + 1]
            return True
        else:
            return True

    def check_chest_collision(self, x, y) -> bool:
        if self.__fields[x][y] == Field.WALL or self.__fields[x][y] == Field.CHEST:
            return False

        return True

    def get_field_based_on_player_pos(self, x, y):
        return self.__fields[self.__player_pos_x + x][self.__player_pos_y + y]

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
