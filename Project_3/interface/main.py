
import copy
import sys
from enum import Enum

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gio, Gtk, GdkPixbuf

INTERFACE_XML = """
<?xml version="1.0"?>
<interface>
  <requires lib="gtk+" version="2.16"/>
  <!-- interface-naming-policy project-wide -->
  <object class="GtkWindow" id="window1">
    <property name="resizable">False</property>
    <property name="default_width">700</property>
    <property name="default_height">500</property>
    <child>
      <object class="GtkVBox" id="vbox1">
        <property name="visible">True</property>
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkMenuBar" id="menubar1">
            <property name="visible">True</property>
            <child>
              <object class="GtkMenuItem" id="menuitem1">
                <property name="visible">True</property>
                <property name="label" translatable="yes">Informacje</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu1">
                    <property name="visible">True</property>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem1">
                        <property name="label" translatable="yes">Opis</property>
                        <property name="visible">True</property>
                        <property name="image">image1</property>
                        <property name="use_stock">False</property>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkFixed" id="fixed1">
            <property name="visible">True</property>
            <child>
              <object class="GtkVButtonBox" id="vbuttonbox1">
                <property name="width_request">144</property>
                <property name="height_request">273</property>
                <property name="visible">True</property>
                <property name="spacing">10</property>
                <child>
                  <object class="GtkButton" id="button1">
                    <property name="label" translatable="yes">Start</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="button2">
                    <property name="label" translatable="yes">Restart</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="button3">
                    <property name="label" translatable="yes">Zapisz</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="button4">
                    <property name="label" translatable="yes">Wczytaj</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="button5">
                    <property name="label" translatable="yes">Plansza &#x142;atwa</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">4</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="button6">
                    <property name="label" translatable="yes">Plansza &#x15B;rednia</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">5</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="button7">
                    <property name="label" translatable="yes">Plansza trudna</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">6</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="button8">
                    <property name="label" translatable="yes">Wyniki</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">7</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="button9">
                    <property name="label" translatable="yes">Resetuj wyniki</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">8</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="x">7</property>
                <property name="y">20</property>
              </packing>
            </child>
            <child>
              <object class="GtkHBox" id="hbox1">
                <property name="width_request">272</property>
                <property name="height_request">48</property>
                <property name="visible">True</property>
                <child>
                  <object class="GtkLabel" id="label1">
                    <property name="visible">True</property>
                    <property name="label" translatable="yes">Plansza:</property>
                  </object>
                  <packing>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="label2">
                    <property name="visible">True</property>
                    <property name="label" translatable="yes">Czas:</property>
                  </object>
                  <packing>
                    <property name="position">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="label3">
                    <property name="visible">True</property>
                    <property name="label" translatable="yes">Wynik:</property>
                  </object>
                  <packing>
                    <property name="position">2</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="x">154</property>
                <property name="y">13</property>
              </packing>
            </child>
            <child>
              <object class="GtkDrawingArea" id="drawingarea1">
                <property name="width_request">100</property>
                <property name="height_request">80</property>
                <property name="visible">True</property>
              </object>
              <packing>
                <property name="x">193</property>
                <property name="y">105</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel" id="label4">
                <property name="width_request">82</property>
                <property name="height_request">20</property>
                <property name="visible">True</property>
                <property name="yalign">0.44999998807907104</property>
                <property name="label" translatable="yes">Wygrana</property>
              </object>
              <packing>
                <property name="x">228</property>
                <property name="y">47</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkImage" id="image1">
    <property name="visible">True</property>
    <property name="stock">gtk-missing-image</property>
  </object>
</interface>

"""


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


class Results():

    def reset_results(self):
        file_name: str = map_game_board_to_result_file_name(GameBoard.EASY)
        if file_name != "":
            with open('..\\results\\' + file_name, "w") as file:
                file.close()

        file_name = map_game_board_to_result_file_name(GameBoard.MED)
        if file_name != "":
            with open('..\\results\\' + file_name, "w") as file:
                file.close()

        file_name = map_game_board_to_result_file_name(GameBoard.HARD)
        if file_name != "":
            with open('..\\results\\' + file_name, "w") as file:
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
            with open('..\\results\\' + file_name, "w") as file:
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

    def add_board_results(self, game_board: GameBoard) -> str:
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
            with open('..\\results\\' + file_name) as file:
                for line in file:
                    results.append(float(line.strip()))

                file.close()

        return results


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
                '..\\boards\\' + file_name) as file:
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


class DialogExample(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, title="Potwierdzenie", transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        self.set_default_size(150, 100)

        label = Gtk.Label(label="Na pewno usunąć zapisane wyniki?")

        box = self.get_content_area()
        box.add(label)
        self.show_all()


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            application_id="org.example.myapp",
            flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
            **kwargs
        )
        self.window = None

        self.add_main_option(
            "test",
            ord("t"),
            GLib.OptionFlags.NONE,
            GLib.OptionArg.NONE,
            "Command line test",
            None,
        )

    def do_startup(self):
        Gtk.Application.do_startup(self)

        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.on_about)
        self.add_action(action)

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)

        self.builder = Gtk.Builder.new_from_string(INTERFACE_XML, -1)
        self.main_window = self.builder.get_object("window1")
        self.main_window.show()

        # my setup
        self.playing: bool = False
        # self.timer = QTimer(MainWindow) todo
        # self.timer.timeout.connect(self.show_time)
        # self.timer.start(100)
        GLib.timeout_add(100, self.show_time)
        self.time = 0
        self.player_can_move = True
        self.results = Results()
        self.game_board = GameBoard.EASY
        self.board = Board(1, 1)
        self.board.load_board_from_file(map_game_board_to_file_name(self.game_board))
        self.easy_bord_save = None
        self.easy_time_save = None
        self.med_bord_save = None
        self.med_time_save = None
        self.hard_bord_save = None
        self.hard_time_save = None

        # buttons
        self.button_start_stop = self.builder.get_object("button1")
        self.button_restart = self.builder.get_object("button2")
        self.button_save = self.builder.get_object("button3")
        self.button_load = self.builder.get_object("button4")
        self.button_easy = self.builder.get_object("button5")
        self.button_med = self.builder.get_object("button6")
        self.button_hard = self.builder.get_object("button7")
        self.button_results = self.builder.get_object("button8")
        self.button_reset_res = self.builder.get_object("button9")
        # labels
        self.label_board = self.builder.get_object("label1")
        self.label_board.set_text("Plansza: poziom " + map_game_board_to_level_name(self.game_board))
        self.label_time = self.builder.get_object("label2")
        self.label_time.set_text("Czas: 0.0")
        self.label_score = self.builder.get_object("label3")
        self.label_score.set_text("Wynik: " + str(self.board.chests_on_goals) + "/" + str(self.board.chests))
        self.label_win = self.builder.get_object("label4")
        #self.label_win.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("green"))

        self.fixed = self.builder.get_object("fixed1")
        self.images = []
        self.pixbuffs = []
        #images
        self.pixbuf_player = GdkPixbuf.Pixbuf.new_from_file("../graphics/player.bmp")
        self.image_player = Gtk.Image()
        self.image_player.set_from_pixbuf(self.pixbuf_player)
        self.pixbuf_wall = GdkPixbuf.Pixbuf.new_from_file("../graphics/wall.bmp")
        self.image_wall = Gtk.Image()
        self.image_wall.set_from_pixbuf(self.pixbuf_wall)
        self.pixbuf_chest = GdkPixbuf.Pixbuf.new_from_file("../graphics/chest.bmp")
        self.image_chest = Gtk.Image()
        self.image_chest.set_from_pixbuf(self.pixbuf_chest)
        self.pixbuf_goal = GdkPixbuf.Pixbuf.new_from_file("../graphics/goal.bmp")
        self.image_goal = Gtk.Image()
        self.image_goal.set_from_pixbuf(self.pixbuf_goal)
        self.pixbuf_empty = GdkPixbuf.Pixbuf.new_from_file("../graphics/empty.bmp")
        self.image_empty = Gtk.Image()
        self.image_empty.set_from_pixbuf(self.pixbuf_empty)
        #self.fixed.put(self.image_player, 10, 10)
        self.print_board()
        self.main_window.connect("key-press-event", self.on_key_press_event)

        #button actions
        self.button_start_stop.connect("clicked", self.start_stop)
        self.button_restart.connect("clicked", self.reset_board)
        self.button_easy.connect("clicked", self.load_easy_board)
        self.button_hard.connect("clicked", self.load_hard_board)
        self.button_med.connect("clicked", self.load_med_board)
        self.button_save.connect("clicked", self.save_game_state)
        self.button_load.connect("clicked", self.load_game_state)
        self.button_results.connect("clicked", self.on_results_clicked)
        self.button_reset_res.connect("clicked", self.on_res_results_clicked)

        self.menu_opis = self.builder.get_object("imagemenuitem1")
        self.menu_opis.connect("activate", self.on_info_clicked)

        self.main_window.show_all()
        self.label_win.hide()
        # self.main_window.add(self.image)
        # self.set_app_menu(builder.get_object("app-menu"))

    def show_time(self):
        if self.playing:
            self.time += 1
            text = "Czas: " + str(self.time / 10) + " s"
            self.label_time.set_text(text)
        return True

    #start and stop counting time pause of the game
    def start_stop(self, widget):
        if not self.label_win.props.visible:
            self.playing = self.playing != True
            self.start_stop_button_text()

    def reset_board(self, widget):
        self.board.load_board_from_file(map_game_board_to_file_name(self.game_board))
        self.time = 0
        self.playing = False
        self.start_stop_button_text()
        self.print_board()
        self.label_win.hide()
        self.player_can_move = True
        text = "Czas: " + str(self.time / 10) + " s"
        self.label_time.set_text(text)

    def load_easy_board(self, widget):
        self.load_board(GameBoard.EASY)

    def load_med_board(self, widget):
        self.load_board(GameBoard.MED)

    def load_hard_board(self, widget):
        self.load_board(GameBoard.HARD)

    #load save of the game
    def load_board(self, game_board: GameBoard):
        self.game_board = game_board
        self.board.load_board_from_file(map_game_board_to_file_name(self.game_board))
        self.time = 0
        self.playing = False
        self.player_can_move = True
        self.print_board()
        self.label_win.hide()
        self.label_board.set_text("Plansza: poziom " + map_game_board_to_level_name(self.game_board))
        text = "Czas: " + str(self.time / 10) + " s"
        self.label_time.set_text(text)

    def save_game_state(self, widget):
        if self.game_board == GameBoard.EASY:
            self.easy_bord_save = copy.deepcopy(self.board)
            self.easy_time_save = copy.deepcopy(self.time)
        elif self.game_board == GameBoard.MED:
            self.med_bord_save = copy.deepcopy(self.board)
            self.med_time_save = copy.deepcopy(self.time)
        elif self.game_board == GameBoard.HARD:
            self.hard_bord_save = copy.deepcopy(self.board)
            self.hard_time_save = copy.deepcopy(self.time)

    def load_game_state(self, widget):
        if self.game_board == GameBoard.EASY and self.easy_bord_save is not None:
            self.load_board_state(self.easy_bord_save, self.easy_time_save)
        elif self.game_board == GameBoard.MED and self.med_bord_save is not None:
            self.load_board_state(self.med_bord_save, self.med_time_save)
        elif self.game_board == GameBoard.HARD and self.hard_bord_save is not None:
            self.load_board_state(self.hard_bord_save, self.hard_time_save)

        self.print_board()
        text = "Czas: " + str(self.time / 10) + " s"
        self.label_time.set_text(text)

    def load_board_state(self, board_save, time_save):
        self.board = copy.deepcopy(board_save)
        self.time = copy.deepcopy(time_save)
        self.playing = True
        self.start_stop(None)
        self.label_win.hide()
        self.player_can_move = True
        self.label_board.set_text("Plansza: poziom " + map_game_board_to_level_name(self.game_board))

    def on_info_clicked(self, widget):
        dialog = Gtk.MessageDialog(
            transient_for=self.main_window,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Opis aplikacji",
        )
        dialog.format_secondary_text(
            "Aplikacja jest implementacją gry Sokoban, która jest to klasyczna gra typu łamigłówki, "
            "w której celem jest odpowiednie ustawienie "
            "skrzyń na polach celu. Plansza składa się z układu kwadratów, na które składają się: ściany, gracz, skrzynie i "
            "cele. Gracz może poruszać skrzynią, ale tylko w kierunku, w którym aktualnie się przemieszcza. "
            "Ściany ograniczają możliwość poruszania się po planszy. Sokoban jest grą, w której gracz musi "
            "przesuwać skrzynie na odpowiednie miejsca, przy jak najmniejszej liczbie wykonanych ruchów lub w "
            "najkrótszym czasie. Gracz może pchać tylko jedną skrzynię, nie można ich ciągnąć ani przez nie "
            "przechodzić \n\nWersja 1.101.2")
        dialog.run()

        dialog.destroy()

    def on_results_clicked(self, widget):
        dialog = Gtk.MessageDialog(
            transient_for=self.main_window,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Wyniki",
        )
        dialog.format_secondary_text(self.results.get_results_text())
        dialog.run()

        dialog.destroy()

    def on_res_results_clicked(self, widget):
        dialog = DialogExample(self.main_window)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            self.results.reset_results()

        dialog.destroy()

    def start_stop_button_text(self):
        if self.playing == True:
            self.button_start_stop.set_label("Stop")
        else:
            self.button_start_stop.set_label("Start")

    def on_key_press_event(self, widget, event):
        if self.player_can_move:
            if event.keyval == 100:
                self.move_player(Direction.RIGHT)
            elif event.keyval == 97:
                self.move_player(Direction.LEFT)
            elif event.keyval == 119:
                self.move_player(Direction.UP)
            elif event.keyval == 115:
                self.move_player(Direction.DOWN)

    def move_player(self, direction: Direction):
        self.playing = True
        self.start_stop_button_text()
        self.board.player_move(direction)
        self.print_board()
        self.label_score.set_text(self.board.return_result())
        if self.board.check_if_player_won():
            self.playing = False
            self.player_can_move = False
            self.results.write_result(self.game_board, self.time / 10)
            self.label_win.show()
        else:
            self.label_win.hide()

    def print_board(self):
        for elem in self.images:
            self.fixed.remove(elem)
            del elem

        for elem in self.pixbuffs:
            del elem

        self.images = []
        self.pixbuffs = []

        pozycjaX = 200
        pozycjaY = 75
        for i in range(0, self.board.get_x()):
            for j in range(0, self.board.get_y()):
                if self.board.fields[i][j] == Field.WALL:
                    self.fixed.put(self.prepare_img('wall.bmp'), pozycjaX, pozycjaY)
                elif self.board.fields[i][j] == Field.EMPTY:
                    self.fixed.put(self.prepare_img('empty.bmp'), pozycjaX, pozycjaY)
                elif self.board.fields[i][j] == Field.GOAL:
                    self.fixed.put(self.prepare_img('goal.bmp'), pozycjaX, pozycjaY)
                elif self.board.fields[i][j] == Field.CHEST:
                    self.fixed.put(self.prepare_img('chest.bmp'), pozycjaX, pozycjaY)
                elif self.board.fields[i][j] == Field.PLAYER:
                    self.fixed.put(self.prepare_img('player.bmp'), pozycjaX, pozycjaY)
                pozycjaX += 40
            pozycjaX = 200
            pozycjaY += 40

        self.main_window.show_all()
        self.label_score.set_text("Wynik: " + str(self.board.chests_on_goals) + "/" + str(self.board.chests))

    def prepare_img(self, file_name: str):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file("../graphics/" + file_name)
        img = Gtk.Image()
        img.set_from_pixbuf(pixbuf)
        self.images.append(img)
        self.pixbuffs.append(pixbuf)

        return img

    def do_activate(self):
        # We only allow a single window and raise any existing ones
        if not self.window:
            # Windows are associated with the application
            # when the last one is closed the application shuts down
            self.window = AppWindow(application=self, title="Main Window")

        # self.window.present()

    def do_command_line(self, command_line):
        options = command_line.get_options_dict()
        # convert GVariantDict -> GVariant -> dict
        options = options.end().unpack()

        if "test" in options:
            # This is printed on the main instance
            print("Test argument recieved: %s" % options["test"])

        self.activate()
        return 0

    def on_about(self, action, param):
        about_dialog = Gtk.AboutDialog(transient_for=self.window, modal=True)
        about_dialog.present()

    def on_quit(self, action, param):
        self.quit()


if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)
