import os
from enum import Enum
from pathlib import Path
from logic.Enums import *


class Board():

    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y
        self.turn = 0
        self.fields = [[Field.EMPTY for i in range(x)] for j in range(y)]
        self.base_fields = [[Field.EMPTY for i in range(x)] for j in range(y)]
        self.player_pos_x = 0
        self.player_pos_y = 0
        self.field_under_player = Field.EMPTY
        self.chests = 0
        self.chests_on_goals = 0

    def set_field_type(self, x, y, field):
        self.fields[x][y] = field

    def player_move(self, direction):
        if direction == Direction.UP and self.check_player_up_collision():
            self.fields[self.player_pos_x][self.player_pos_y] = self.field_under_player
            self.player_pos_x -= 1
            self.move_player()

        elif direction == Direction.DOWN and self.check_player_down_collision():
            self.fields[self.player_pos_x][self.player_pos_y] = self.field_under_player
            self.player_pos_x += 1
            self.move_player()

        elif direction == Direction.LEFT and self.check_player_left_collision():
            self.fields[self.player_pos_x][self.player_pos_y] = self.field_under_player
            self.player_pos_y -= 1
            self.move_player()

        elif direction == Direction.RIGHT and self.check_player_right_collision():
            self.fields[self.player_pos_x][self.player_pos_y] = self.field_under_player
            self.player_pos_y += 1
            self.move_player()

    def move_player(self):
        self.field_under_player = self.fields[self.player_pos_x][self.player_pos_y]
        self.fields[self.player_pos_x][self.player_pos_y] = Field.PLAYER
        self.count_chests_on_goals()

    def check_player_up_collision(self) -> bool:
        if self.get_field_based_on_player_pos(-1, 0) == Field.WALL:
            return False
        elif self.get_field_based_on_player_pos(-1, 0) == Field.CHEST:
            if self.check_chest_collision(self.player_pos_x - 2, self.player_pos_y):
                self.fields[self.player_pos_x - 2][self.player_pos_y] = Field.CHEST
                self.fields[self.player_pos_x - 1][self.player_pos_y] = self.base_fields[self.player_pos_x - 1][
                    self.player_pos_y]
                return True
            else:
                return False
        else:
            return True

    def check_player_down_collision(self) -> bool:
        if self.get_field_based_on_player_pos(1, 0) == Field.WALL:
            return False
        elif self.get_field_based_on_player_pos(1, 0) == Field.CHEST:
            if self.check_chest_collision(self.player_pos_x + 2, self.player_pos_y):
                self.fields[self.player_pos_x + 2][self.player_pos_y] = Field.CHEST
                self.fields[self.player_pos_x + 1][self.player_pos_y] = self.base_fields[self.player_pos_x + 1][
                    self.player_pos_y]
                return True
            else:
                return False
        else:
            return True

    def check_player_left_collision(self) -> bool:
        if self.get_field_based_on_player_pos(0, -1) == Field.WALL:
            return False
        elif self.get_field_based_on_player_pos(0, -1) == Field.CHEST:
            if self.check_chest_collision(self.player_pos_x, self.player_pos_y - 2):
                self.fields[self.player_pos_x][self.player_pos_y - 2] = Field.CHEST
                self.fields[self.player_pos_x][self.player_pos_y - 1] = self.base_fields[self.player_pos_x][
                    self.player_pos_y - 1]
                return True
            else:
                return False
        else:
            return True

    def check_player_right_collision(self) -> bool:
        if self.get_field_based_on_player_pos(0, 1) == Field.WALL:
            return False
        elif self.get_field_based_on_player_pos(0, 1) == Field.CHEST:
            if self.check_chest_collision(self.player_pos_x, self.player_pos_y + 2):
                self.fields[self.player_pos_x][self.player_pos_y + 2] = Field.CHEST
                self.fields[self.player_pos_x][self.player_pos_y + 1] = self.base_fields[self.player_pos_x][
                    self.player_pos_y + 1]
                return True
            else:
                return False
        else:
            return True

    def check_chest_collision(self, x, y) -> bool:
        if self.fields[x][y] == Field.WALL or self.fields[x][y] == Field.CHEST:
            return False

        return True

    def get_field_based_on_player_pos(self, x, y):
        return self.fields[self.player_pos_x + x][self.player_pos_y + y]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_turn(self):
        return self.turn

    def get_board(self):
        return self.fields

    def initialize_board_fields(self, x, y):
        self.x = x
        self.y = y
        self.turn = 0
        self.fields = [[Field.EMPTY for i in range(x)] for j in range(y)]
        self.base_fields = [[Field.EMPTY for i in range(x)] for j in range(y)]
        self.player_pos_x = 0
        self.player_pos_y = 0
        self.field_under_player = Field.EMPTY

    def load_board_from_file(self, file_name):
        with open(
                os.path.dirname(Path(__file__).parent) + '\\boards\\' + file_name) as file:
            x = int(file.readline().strip())
            y = int(file.readline().strip())
            self.chests = 0
            self.chests_on_goals = 0
            self.initialize_board_fields(x, y)
            for i in range(0, self.x):
                for j in range(0, self.y):
                    read_field = int(file.read(1))
                    self.fields[i][j] = Field(int(read_field))
                    self.base_fields[i][j] = Field(int(read_field))
                    if read_field == 3:
                        self.base_fields[i][j] = Field.WALL
                        self.player_pos_x = i
                        self.player_pos_y = j

                    if read_field == 2:
                        self.base_fields[i][j] = Field.EMPTY
                        self.chests += 1

            file.close()

    def check_if_player_won(self) -> bool:
        return self.chests == self.chests_on_goals

    def count_chests_on_goals(self):
        self.chests_on_goals = 0
        for i in range(0, self.x):
            for j in range(0, self.y):
                if self.fields[i][j] == Field.CHEST and self.base_fields[i][j] == Field.GOAL:
                    self.chests_on_goals += 1

    def return_result(self) -> str:
        return 'Wynik: ' + str(self.chests_on_goals) + ' z ' + str(self.chests)



