import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout, QLineEdit, QPushButton, QMessageBox,
                             QDesktopWidget, QLabel, QMainWindow, QStackedLayout, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.Qt import  QColor


class MainGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.create_main_menu_layout()

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.main_menu_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("ToolBox")
        self.setWindowIcon(QIcon('CornerIcon.png'))

        self.show()


    def create_main_menu_layout(self):
        self.math_btn = QPushButton('Math', self)
        self.phys_btn = QPushButton('Physics', self)
        self.chem_btn = QPushButton('Chemistry', self)
        self.fav_btn = QPushButton('Favorites', self)

        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.math_btn)
        self.initial_layout.addWidget(self.phys_btn)
        self.initial_layout.addWidget(self.chem_btn)
        self.initial_layout.addWidget(self.fav_btn)

        self.math_btn.clicked.connect(self.buttonClickHandler)
        self.phys_btn.clicked.connect(self.buttonClickHandler)
        self.chem_btn.clicked.connect(self.buttonClickHandler)
        self.fav_btn.clicked.connect(self.buttonClickHandler)

        self.main_menu_widget = QWidget()
        self.main_menu_widget.setLayout(self.initial_layout)
        self.show()

    def create_math_menu(self):

        input_one_label = QLabel('Input One')
        input_two_label = QLabel('Input Two')
        output_label = QLabel('Output')

        input_one = QLineEdit()
        input_two = QLineEdit()
        output = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(input_one_label, 1, 0)
        grid.addWidget(input_one, 1, 1)

        grid.addWidget(input_two_label, 2, 0)
        grid.addWidget(input_two, 2, 1)

        btn = QPushButton('Calculate', self)

        grid.addWidget(btn, 3, 1, 1, 1)

        grid.addWidget(output_label, 4, 0)
        grid.addWidget(output, 4, 1)

        btn.clicked.connect(calculate_clicked)

        math_menu_widget = QWidget()
        math_menu_widget.setLayout(grid)
        self.show()

        def calculate_clicked(self):
            i_one = input_one.text()
            i_two = input_two.text()

            if i_one.isnumeric() & i_two.isnumeric():
                in_one = int(i_one)
                in_two = int(i_two)

                out_sum = in_one + in_two
                self.output.setText(str(out_sum))


    def buttonClickHandler(self):

        if self.sender() == self.math_btn:
            self.create_math_menu()
            self.stacked_layout.addWidget(self.math_menu_widget)
            self.stacked_layout.setCurrentIndex(1)
        elif self.sender() == self.phys_btn:
            self.label.setText("physics was pressed")
        elif self.sender() == self.chem_btn:
            self.label.setText("chemistry was pressed")
        elif self.sender() == self.fav_btn:
            self.label.setText("favorites was pressed")
        else:
            self.label.setText("not working")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mm = MainGUI()
    sys.exit(app.exec_())