import os
from enum import Enum
from pathlib import Path
from logic.Enums import *

from logic.Mappers import map_game_board_to_result_file_name


class Results():

    def reset_results(self):
        file_name: str = map_game_board_to_result_file_name(GameBoard.EASY)
        if file_name != "":
            with open(os.path.dirname(Path(__file__).parent) + '\\results\\' + file_name, "w") as file:
                file.close()

        file_name = map_game_board_to_result_file_name(GameBoard.MED)
        if file_name != "":
            with open(os.path.dirname(Path(__file__).parent) + '\\results\\' + file_name, "w") as file:
                file.close()

        file_name = map_game_board_to_result_file_name(GameBoard.HARD)
        if file_name != "":
            with open(os.path.dirname(Path(__file__).parent) + '\\results\\' + file_name, "w") as file:
                file.close()

    def write_result(self, game_board: GameBoard, time: float):
        file_name: str = map_game_board_to_result_file_name(game_board)
        res: list = self.get_results(file_name)
        for res_elem in res:
            if res_elem > time and len(res) == 3:
                res[2] = time
                break
            elif res_elem > time:
                res.append(time)
                break

        if len(res) == 0:
            res.append(time)

        if file_name != "":
            with open(os.path.dirname(Path(__file__).parent) + '\\results\\' + file_name, "w") as file:
                for res_elem in sorted(res):
                    file.write(str(res_elem) + '\n')

            file.close()

    def get_results_text(self) -> str:
        text: str = "Plansza łatwa:\n"
        text += self.add_board_results(GameBoard.EASY)
        text += "\nPlansza średnia:\n"
        text += self.add_board_results(GameBoard.MED)
        text += "\nPlansza trudna:\n"
        text += self.add_board_results(GameBoard.HARD)

        return text

    def add_board_results(self,game_board: GameBoard) -> str:
        text: str = ""
        iter = 0
        for res in self.get_results(map_game_board_to_result_file_name(game_board)):
            iter += 1
            text += str(iter) + ". " + str(res) + "\n"

        for iter in range(iter + 1, 4):
            text += str(iter) + ".\n"

        return text

    def get_results(self, file_name: str) -> list:
        results = []
        if file_name != "":
            with open(os.path.dirname(Path(__file__).parent) + '\\results\\' + file_name) as file:
                for line in file:
                    results.append(float(line.strip()))

                file.close()

        return results

