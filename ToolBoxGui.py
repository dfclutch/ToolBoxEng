import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout, QLineEdit, QPushButton, QMessageBox,
                             QDesktopWidget, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.Qt import  QColor


class MainMenu(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.math_btn = QPushButton('Math', self)
        self.phys_btn = QPushButton('Physics', self)
        self.chem_btn = QPushButton('Chemistry', self)
        self.fav_btn = QPushButton('Favorites', self)

        self.math_btn.clicked.connect(self.buttonClickHandler)
        self.phys_btn.clicked.connect(self.buttonClickHandler)
        self.chem_btn.clicked.connect(self.buttonClickHandler)
        self.fav_btn.clicked.connect(self.buttonClickHandler)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.math_btn, 0, 0)
        grid.addWidget(self.phys_btn, 1, 0)
        grid.addWidget(self.chem_btn, 2, 0)
        grid.addWidget(self.fav_btn, 3, 0)

        self.setLayout(grid)

        self.label = QLabel('Press A Button')
        grid.addWidget(self.label)

        self.resize(800, 600)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#e3f4fc'))
        self.setPalette(p)

        self.center()
        self.setWindowTitle("ToolBox")
        self.setWindowIcon(QIcon('CornerIcon.png'))

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to Quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def buttonClickHandler(self):

        if self.sender() == self.math_btn:
            TB = ToolBoxGui.ToolBox()
            TB.show()
        elif self.sender() == self.phys_btn:
            self.label.setText("physics was pressed")
        elif self.sender() == self.chem_btn:
            self.label.setText("chemistry was pressed")
        elif self.sender() == self.fav_btn:
            self.label.setText("favorites was pressed")
        else:
            self.label.setText("not working")

class ToolBox(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()



    def init_ui(self):

        input_one_label = QLabel('Input One')
        input_two_label = QLabel('Input Two')
        output_label = QLabel('Output')

        self.input_one = QLineEdit()
        self.input_two = QLineEdit()
        self.output = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(input_one_label, 1, 0)
        grid.addWidget(self.input_one, 1, 1)

        grid.addWidget(input_two_label, 2, 0)
        grid.addWidget(self.input_two, 2, 1)

        btn = QPushButton('Calculate', self)

        grid.addWidget(btn, 3, 1, 1, 1)

        grid.addWidget(output_label, 4, 0)
        grid.addWidget(self.output, 4, 1)

        btn.clicked.connect(self.calculate_clicked)

        self.setLayout(grid)

        self.resize(800, 600)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#e3f4fc'))
        self.setPalette(p)

        self.center()
        self.setWindowTitle("ToolBox")
        self.setWindowIcon(QIcon('CornerIcon.png'))

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to Quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def calculate_clicked(self):
        i_one = self.input_one.text()
        i_two = self.input_two.text()

        if i_one.isnumeric() & i_two.isnumeric():
            in_one = int(i_one)
            in_two = int(i_two)

            out_sum = in_one + in_two
            self.output.setText(str(out_sum))

# main method #
if __name__ == '__main__':

    app = QApplication(sys.argv)
    tb = ToolBox()
    sys.exit(app.exec_())