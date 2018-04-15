import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout, QLineEdit, QPushButton, QMessageBox,
                             QDesktopWidget, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.Qt import  QColor


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
        p.setColor(self.backgroundRole(), QColor('#e2f4fc'))
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