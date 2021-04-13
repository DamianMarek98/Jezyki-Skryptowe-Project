import copy
from copyreg import pickle

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt, QTimer
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QAction, QMessageBox

from logic.Board import Board
from logic.Enums import GameBoard, Direction, Field
from logic.Mappers import map_game_board_to_file_name, map_game_board_to_level_name
from results.Results import Results


class Ui_MainWindow(object):
    #window set up - controlls and widgets generated
    def setupUi(self, MainWindow):
        self.playing: bool = False
        self.timer = QTimer(MainWindow)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(100)
        self.time = 0
        self.player_can_move = True
        self.results = Results()
        self.game_board = GameBoard.EASY
        self.board = Board(1, 1)
        self.board.load_board_from_file(map_game_board_to_file_name(self.game_board))
        self.easy_bord_save= None
        self.easy_time_save = None
        self.med_bord_save= None
        self.med_time_save = None
        self.hard_bord_save= None
        self.hard_time_save = None

        MainWindow.setObjectName("Sokoban")
        MainWindow.setFixedWidth(700)
        MainWindow.setFixedHeight(500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vertical_menu = QtWidgets.QWidget(self.centralwidget)
        self.vertical_menu.setGeometry(QtCore.QRect(0, 20, 211, 311))
        self.vertical_menu.setObjectName("verticalLayoutWidget")

        self.game_info_layout = QtWidgets.QVBoxLayout(self.vertical_menu)
        self.game_info_layout.setContentsMargins(0, 0, 0, 0)
        self.game_info_layout.setObjectName("verticalLayout_2")
        self.start_stop_button = QtWidgets.QPushButton(self.vertical_menu)

        self.start_stop_button.clicked.connect(self.start_stop)
        self.start_stop_button.setObjectName("pushButton_7")
        self.game_info_layout.addWidget(self.start_stop_button)

        self.reset_button = QtWidgets.QPushButton(self.vertical_menu)
        self.reset_button.setObjectName("pushButton_2")
        self.game_info_layout.addWidget(self.reset_button)
        self.reset_button.clicked.connect(self.reset_board)

        self.save_button = QtWidgets.QPushButton(self.vertical_menu)
        self.save_button.setObjectName("pushButton_9")
        self.game_info_layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_game_state)

        self.load_button = QtWidgets.QPushButton(self.vertical_menu)
        self.load_button.setObjectName("pushButton_8")
        self.game_info_layout.addWidget(self.load_button)
        self.load_button.clicked.connect(self.load_game_state)

        self.button_easy_board = QtWidgets.QPushButton(self.vertical_menu)
        self.button_easy_board.clicked.connect(self.load_easy_board)
        self.button_easy_board.setObjectName("pushButton_4")
        self.game_info_layout.addWidget(self.button_easy_board)

        self.button_med_board = QtWidgets.QPushButton(self.vertical_menu)
        self.button_med_board.setObjectName("pushButton_3")
        self.button_med_board.clicked.connect(self.load_med_board)
        self.game_info_layout.addWidget(self.button_med_board)

        self.button_hard_board = QtWidgets.QPushButton(self.vertical_menu)
        self.button_hard_board.clicked.connect(self.load_hard_board)
        self.button_hard_board.setObjectName("pushButton")
        self.game_info_layout.addWidget(self.button_hard_board)

        self.button_results = QtWidgets.QPushButton(self.vertical_menu)
        self.button_results.setObjectName("pushButton_5")
        self.button_results.clicked.connect(self.action_results)
        self.game_info_layout.addWidget(self.button_results)

        self.button_reset_results = QtWidgets.QPushButton(self.vertical_menu)
        self.button_reset_results.setObjectName("pushButton_6")
        self.button_reset_results.clicked.connect(self.action_reset_results)
        self.game_info_layout.addWidget(self.button_reset_results)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 10, 451, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_poziom_planszy = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_poziom_planszy.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_poziom_planszy)

        self.label_time = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_time.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_time)

        self.label_score = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_score.setObjectName("label")
        self.horizontalLayout.addWidget(self.label_score)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 21))
        self.menubar.setObjectName("menubar")
        self.menu_info = QtWidgets.QMenu(self.menubar)
        self.menu_info.setObjectName("menuinformacje")
        self.menu_action = QAction('Opis')
        self.menu_action.triggered.connect(self.action_info)
        self.menu_info.addAction(self.menu_action)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_info.menuAction())
        self.win_label = QtWidgets.QLabel('WYGRANA', self.centralwidget)
        self.win_label.setStyleSheet("color: green")
        self.win_label.move((MainWindow.window().width() - self.win_label.width()) / 2, 42)
        self.win_label.hide()
        self.horizontal_group_box = QGroupBox("")
        MainWindow.layout().addWidget(self.horizontal_group_box)
        self.print_board()

        MainWindow.keyPressEvent = self.keyPressEvent

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #displays informations about app
    def action_info(self):
        msg = QMessageBox()
        msg.setWindowTitle("Opis aplikacji")
        msg.setText("Aplikacja jest implementacją gry Sokoban, która jest to klasyczna gra typu łamigłówki, "
                    "w której celem jest odpowiednie ustawienie "
                    "skrzyń na polach celu. Plansza składa się z układu kwadratów, na które składają się: ściany, gracz, skrzynie i "
        "cele. Gracz może poruszać skrzynią, ale tylko w kierunku, w którym aktualnie się przemieszcza. "
        "Ściany ograniczają możliwość poruszania się po planszy. Sokoban jest grą, w której gracz musi "
        "przesuwać skrzynie na odpowiednie miejsca, przy jak najmniejszej liczbie wykonanych ruchów lub w "
        "najkrótszym czasie. Gracz może pchać tylko jedną skrzynię, nie można ich ciągnąć ani przez nie "
        "przechodzić \n\nWersja 1.101.2")
        msg.exec()

    #displays results
    def action_results(self):
        msg = QMessageBox()
        msg.setWindowTitle("Wyniki")
        msg.setText(self.results.get_results_text())
        msg.exec()

    def action_reset_results(self):
        ret = QMessageBox.question(MainWindow, "Potwierdzenie", "Na pewno usunąć zapisane wyniki?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ret == QMessageBox.Yes:
            self.results.reset_results()

    #start and stop counting time pause of the game
    def start_stop(self):
        if self.win_label.isHidden():
            self.playing = self.playing != True
            self.start_stop_button_text()

    def start_stop_button_text(self):
            if self.playing == True:
                self.start_stop_button.setText("Stop")
            else:
                self.start_stop_button.setText("Start")

    #Displays time
    def show_time(self):
        if self.playing:
            self.time += 1
            text = "Czas: " + str(self.time / 10) + " s"
            self.label_time.setText(text)

    #reloads board
    def reset_board(self):
        self.board.load_board_from_file(map_game_board_to_file_name(self.game_board))
        self.time = 0
        self.playing = False
        self.start_stop_button_text()
        self.print_board()
        self.win_label.setHidden(True)
        self.player_can_move = True
        text = "Czas: " + str(self.time / 10) + " s"
        self.label_time.setText(text)

    def load_easy_board(self):
        self.load_board(GameBoard.EASY)

    def load_med_board(self):
        self.load_board(GameBoard.MED)

    def load_hard_board(self):
        self.load_board(GameBoard.HARD)

    #load save of the game
    def load_board(self, game_board: GameBoard):
        self.game_board = game_board
        self.board.load_board_from_file(map_game_board_to_file_name(self.game_board))
        self.time = 0
        self.playing = False
        self.win_label.setHidden(True)
        self.player_can_move = True
        self.print_board()
        self.label_poziom_planszy.setText("Plansza: poziom " + map_game_board_to_level_name(self.game_board))
        text = "Czas: " + str(self.time / 10) + " s"
        self.label_time.setText(text)

    def save_game_state(self):
        if self.game_board == GameBoard.EASY:
            self.easy_bord_save = copy.deepcopy(self.board)
            self.easy_time_save = copy.deepcopy(self.time)
        elif self.game_board == GameBoard.MED:
            self.med_bord_save = copy.deepcopy(self.board)
            self.med_time_save = copy.deepcopy(self.time)
        elif self.game_board == GameBoard.HARD:
            self.hard_bord_save = copy.deepcopy(self.board)
            self.hard_time_save = copy.deepcopy(self.time)

    def load_game_state(self):
        if self.game_board == GameBoard.EASY and self.easy_bord_save is not None:
            self.load_board_state(self.easy_bord_save, self.easy_time_save)
        elif self.game_board == GameBoard.MED and self.med_bord_save is not None:
            self.load_board_state(self.med_bord_save, self.med_time_save)
        elif self.game_board == GameBoard.HARD and self.hard_bord_save is not None:
            self.load_board_state(self.hard_bord_save, self.hard_time_save)

        self.print_board()
        text = "Czas: " + str(self.time / 10) + " s"
        self.label_time.setText(text)

    def load_board_state(self, board_save, time_save):
        self.board = copy.deepcopy(board_save)
        self.time = copy.deepcopy(time_save)
        self.playing = True
        self.start_stop()
        self.win_label.setHidden(True)
        self.player_can_move = True
        self.label_poziom_planszy.setText("Plansza: poziom " + map_game_board_to_level_name(self.game_board))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            MainWindow.close()

        if self.player_can_move == True:
            if event.key() == Qt.Key_W or event.key() == Qt.Key_Up:
                self.move_player(Direction.UP)
            elif event.key() == Qt.Key_S or event.key() == Qt.Key_Down:
                self.move_player(Direction.DOWN)
            elif event.key() == Qt.Key_A or event.key() == Qt.Key_Left:
                self.move_player(Direction.LEFT)
            elif event.key() == Qt.Key_D or event.key() == Qt.Key_Right:
                self.move_player(Direction.RIGHT)

    def move_player(self, direction: Direction):
        self.playing = True
        self.start_stop_button_text()
        self.board.player_move(direction)
        self.print_board()
        self.label_score.setText(self.board.return_result())
        if self.board.check_if_player_won():
            self.playing = False
            self.player_can_move = False
            self.results.write_result(self.game_board, self.time / 10)
            self.win_label.setHidden(False)

    #prints board on it's grid
    def print_board(self):
        MainWindow.layout().removeWidget(self.horizontal_group_box)
        self.horizontal_group_box = QGroupBox("")
        layout = QGridLayout()
        for i in range(0, self.board.get_x()):
            for j in range(0, self.board.get_y()):
                if self.board.fields[i][j] == Field.WALL:
                    layout.addWidget(self.prepare_img('wall.bmp'), i, j)
                elif self.board.fields[i][j] == Field.EMPTY:
                    layout.addWidget(self.prepare_img('empty.bmp'), i, j)
                elif self.board.fields[i][j] == Field.GOAL:
                    layout.addWidget(self.prepare_img('goal.bmp'), i, j)
                elif self.board.fields[i][j] == Field.CHEST:
                    layout.addWidget(self.prepare_img('chest.bmp'), i, j)
                elif self.board.fields[i][j] == Field.PLAYER:
                    layout.addWidget(self.prepare_img('player.bmp'), i, j)

        self.horizontal_group_box.setLayout(layout)
        self.horizontal_group_box.setGeometry(QtCore.QRect(250, 75, 400, 400))
        MainWindow.layout().addWidget(self.horizontal_group_box)
        self.label_score.setText(self.board.return_result())

    def prepare_img(self, file_name: str):
        img = QtWidgets.QLabel(self.centralwidget)
        img.setText("")
        img.setPixmap(QtGui.QPixmap("../graphics/" + file_name))
        img.setScaledContents(True)
        img.setObjectName("test")
        return img

    #generated automaticlly
    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sokoban"))
        self.start_stop_button.setText(_translate("MainWindow", "Start"))
        self.reset_button.setText(_translate("MainWindow", "Restart"))
        self.load_button.setText(_translate("MainWindow", "Wczytaj"))
        self.save_button.setText(_translate("MainWindow", "Zapisz"))
        self.button_easy_board.setText(_translate("MainWindow", "Plansza łatwa"))
        self.button_med_board.setText(_translate("MainWindow", "Plansza średnia"))
        self.button_hard_board.setText(_translate("MainWindow", "Plansza trudna"))
        self.button_results.setText(_translate("MainWindow", "Wyniki"))
        self.button_reset_results.setText(_translate("MainWindow", "Resetuj wyniki"))
        self.label_poziom_planszy.setText(
            _translate("MainWindow", "Plansza: poziom " + map_game_board_to_level_name(self.game_board)))
        self.label_time.setText(_translate("MainWindow", "Czas: 0.0"))
        self.label_score.setText(
            _translate("MainWindow", "Wynik: " + str(self.board.chests_on_goals) + "/" + str(self.board.chests)))
        self.menu_info.setTitle(_translate("MainWindow", "Informacje"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
