from results.Results import GameBoard


def map_game_board_to_result_file_name(game_board: GameBoard) -> str:
    if game_board == GameBoard.EASY:
        return "easy_board_results.txt"
    elif game_board == GameBoard.MED:
        return "med_board_results.txt"
    elif game_board == GameBoard.HARD:
        return "hard_board_results.txt"

    return ""


def map_game_board_to_file_name(game_board: GameBoard) -> str:
    if game_board == GameBoard.EASY:
        return "easy_board.txt"
    elif game_board == GameBoard.MED:
        return "med_board.txt"
    elif game_board == GameBoard.HARD:
        return "hard_board.txt"

    return ""

def map_game_board_to_level_name(game_board: GameBoard) -> str:
    if game_board == GameBoard.EASY:
        return "łatwy"
    elif game_board == GameBoard.MED:
        return "średni"
    elif game_board == GameBoard.HARD:
        return "trudny"

    return ""
