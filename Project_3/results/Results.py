import os
from enum import Enum
from pathlib import Path
from logic.Enums import *

from logic.Mappers import map_game_board_to_result_file_name


class Results():

    def write_result(self, game_board: GameBoard, time: float):
        from logic.Mappers import map_game_board_to_file_name
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

    def get_results(self, game_board: GameBoard) -> list:
        return self.get_results(self.map_game_board_to_result_file_name(game_board))

    def get_results(self, file_name: str) -> list:
        results = []
        if file_name != "":
            with open(os.path.dirname(Path(__file__).parent) + '\\results\\' + file_name) as file:
                for line in file:
                    results.append(float(line.strip()))

                file.close()

        return results


