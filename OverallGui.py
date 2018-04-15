import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout, QLineEdit, QPushButton, QMessageBox,
                             QDesktopWidget, QLabel, QMainWindow, QStackedLayout, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.Qt import  QColor


class MainGUI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.stacked_layout = QStackedLayout()

        self.create_main_menu_layout()
        self.stacked_layout.addWidget(self.main_menu_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

        self.setWindowIcon(QIcon('CornerIcon.png'))

        self.addPages()

    def addPages(self):
        self.create_math_menu()
        self.stacked_layout.addWidget(self.math_menu)
        self.create_phys_menu()
        self.stacked_layout.addWidget(self.phys_menu)
        self.create_chem_menu()
        self.stacked_layout.addWidget(self.chem_menu)
        self.create_fav_menu()
        self.stacked_layout.addWidget(self.fav_menu)
        self.create_add_widget()
        self.stacked_layout.addWidget(self.add_widget)


        self.stacked_layout.setCurrentIndex(0)

    def create_main_menu_layout(self):
        """Creates main menu"""
        self.main_menu_stack_position = 0
        self.math_btn = QPushButton('Math', self)
        self.phys_btn = QPushButton('Physics', self)
        self.chem_btn = QPushButton('Chemistry', self)
        self.fav_btn = QPushButton('Favorites', self)

        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.math_btn)
        self.initial_layout.addWidget(self.phys_btn)
        self.initial_layout.addWidget(self.chem_btn)
        self.initial_layout.addWidget(self.fav_btn)

        self.math_btn.clicked.connect(self.MainMenuButtonClickHandler)
        self.phys_btn.clicked.connect(self.MainMenuButtonClickHandler)
        self.chem_btn.clicked.connect(self.MainMenuButtonClickHandler)
        self.fav_btn.clicked.connect(self.MainMenuButtonClickHandler)

        self.main_menu_widget = QWidget()
        self.main_menu_widget.setLayout(self.initial_layout)
        self.show()

    def create_math_menu(self):
        """Math Submenu"""
        self.math_menu_stack_position = 1

        # build buttons and
        label = QLabel('Math Menu')
        self.add_widget_btn = QPushButton('Add', self)
        self.add_widget_btn.clicked.connect(self.MathMenuButtonClickHandler)
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.backButton(self.main_menu_stack_position))

        # create layout
        self.math_menu_layout = QVBoxLayout()
        self.math_menu_layout.addWidget(label)
        self.math_menu_layout.addWidget(self.add_widget_btn)
        self.math_menu_layout.addWidget(back_btn)


        # create stack object

        self.math_menu = QWidget()
        self.math_menu.setLayout(self.math_menu_layout)
        self.show()

    def create_phys_menu(self):
        """phys Submenu"""
        self.phys_menu_stack_position = 2
        # buttons for physics subwidgets
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.backButton(self.main_menu_stack_position))
        label = QLabel('Physics')

        # create layout
        self.phys_menu_layout = QVBoxLayout()
        self.phys_menu_layout.addWidget(label)
        self.phys_menu_layout.addWidget(back_btn)

        # create stack object
        self.phys_menu = QWidget()
        self.phys_menu.setLayout(self.phys_menu_layout)
        self.show()

    def create_chem_menu(self):
        """phys Submenu"""
        self.chem_menu_stack_position = 3
        # buttons for physics subwidgets
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.backButton(self.main_menu_stack_position))
        label = QLabel('Chemistry')

        # create layout
        self.chem_menu_layout = QVBoxLayout()
        self.chem_menu_layout.addWidget(label)
        self.chem_menu_layout.addWidget(back_btn)

        # create stack object
        self.chem_menu = QWidget()
        self.chem_menu.setLayout(self.chem_menu_layout)
        self.show()

    def create_fav_menu(self):
        """phys Submenu"""
        self.fav_menu_stack_position = 4
        # buttons for physics subwidgets
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.backButton(self.main_menu_stack_position))
        label = QLabel('Favorites')

        # create layout
        self.fav_menu_layout = QVBoxLayout()
        self.fav_menu_layout.addWidget(label)
        self.fav_menu_layout.addWidget(back_btn)

        # create stack object
        self.fav_menu = QWidget()
        self.fav_menu.setLayout(self.fav_menu_layout)
        self.show()

    def create_add_widget(self):
        """Widget for adding numbers"""
        self.add_widget_stack_position = 5
        # build stack widget
        self.add_widget = QWidget()
        # create inputs and outputs
        input_one_label = QLabel('Input One')
        input_two_label = QLabel('Input Two')
        output_label = QLabel('Output')

        self.input_one = QLineEdit()
        self.input_two = QLineEdit()
        self.output = QLineEdit()

        # setup gridlayout
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(input_one_label, 1, 0)
        grid.addWidget(self.input_one, 1, 1)

        grid.addWidget(input_two_label, 2, 0)
        grid.addWidget(self.input_two, 2, 1)

        calc_btn = QPushButton('Calculate', self)
        calc_btn.clicked.connect(self.add_widget_calculate)

        grid.addWidget(calc_btn, 3, 1, 1, 1)

        grid.addWidget(output_label, 4, 0)
        grid.addWidget(self.output, 4, 1)

        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.backButton(self.math_menu_stack_position))
        grid.addWidget(back_btn, 5, 0)


        self.add_widget.setLayout(grid)
        self.show()

    def add_widget_calculate(self):
        """calculates sum for add widget"""
        i_one = self.input_one.text()
        i_two = self.input_two.text()

        if i_one.isnumeric() & i_two.isnumeric():
            in_one = int(i_one)
            in_two = int(i_two)

            out_sum = in_one + in_two
            self.output.setText(str(out_sum))

    def MathMenuButtonClickHandler(self):
        """Handles math submenu button clicks"""
        if self.sender() == self.add_widget_btn:
            self.stacked_layout.setCurrentIndex(self.add_widget_stack_position)

    def MainMenuButtonClickHandler(self):
        """Handles main menu button clicks, directs user to selected submenu"""
        if self.sender() == self.math_btn:
            self.stacked_layout.setCurrentIndex(self.math_menu_stack_position)

        elif self.sender() == self.phys_btn:
            self.stacked_layout.setCurrentIndex(self.phys_menu_stack_position)

        elif self.sender() == self.chem_btn:
            self.stacked_layout.setCurrentIndex(self.chem_menu_stack_position)

        elif self.sender() == self.fav_btn:
            self.stacked_layout.setCurrentIndex(self.fav_menu_stack_position)

    def backButton(self, index):
        """Goes back in the layout stack"""
        self.stacked_layout.setCurrentIndex(index)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mm = MainGUI()
    sys.exit(app.exec_())