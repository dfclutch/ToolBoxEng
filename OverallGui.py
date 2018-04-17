import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout, QLineEdit, QPushButton, QMessageBox, QSplashScreen,
                             QDesktopWidget, QLabel, QMainWindow, QStackedLayout, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import *
from PyQt5.Qt import  QColor
from PyQt5.QtCore import *
import MathToolWidgets
import time


class MainGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Engineering Toolbox'
        self.left = 100
        self.top = 100
        self.width = 900
        self.height = 750
        self.initUI()
        self.stacked_layout = QStackedLayout()

        self.create_main_menu_layout()
        self.stacked_layout.addWidget(self.main_menu_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

        self.setWindowIcon(QIcon('CornerIcon.png'))

        self.addPages()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#444039'))
        self.setPalette(p)
        self.setStyleSheet("""
            QPushButton[menuButton = "true"]{
                border: 1px solid #293744;
                border-radius: 5px;
                padding: 10px 20px;
                background-color: #ff9400;
                min-width: 50px;
                min-height: 100px;
                font-family: "Helvetica";
                font-size: 48px;
            }
            
            QPushButton[menuButton = "false"] {
                border: 1px solid #293744;
                border-radius: 5px;
                padding: 5px 20px;
                background-color: #ff9400;
                min-width: 50px;
                min-height: 80px;
                font-family: "Helvetica";
                font-size: 32px;           
            }
            
            QLabel {   
                font-family: "Helvetica";
                font-size: 36px;    
                color: white;        
            }
            
            QWidget {
                padding: 20px;
            }
            
            QLineEdit {
                font-size: 32px;
                font-family: "Helvetica";
            }   
                                    """)
        self.show()
    def addPages(self):
        """Adds pages to stack in order of their stack position"""
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
        self.create_power_widget()
        self.stacked_layout.addWidget(self.power_widget)
        self.create_integral_widget()
        self.stacked_layout.addWidget(self.integral_widget)

        self.stacked_layout.setCurrentIndex(0)


    """
        MAIN MENU AND MAIN MENU HELPER CLASSES
    """
    def create_main_menu_layout(self):
        """Creates main menu"""
        self.main_menu_stack_position = 0
        self.menu_math_btn = QPushButton('Math', self)
        self.menu_math_btn.setProperty("menuButton", True)
        self.menu_phys_btn = QPushButton('Physics', self)
        self.menu_phys_btn.setProperty("menuButton", True)
        self.menu_chem_btn = QPushButton('Chemistry', self)
        self.menu_chem_btn.setProperty("menuButton", True)
        self.menu_fav_btn = QPushButton('Favorites', self)
        self.menu_fav_btn.setProperty("menuButton", True)

        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.menu_math_btn)
        self.initial_layout.addWidget(self.menu_phys_btn)
        self.initial_layout.addWidget(self.menu_chem_btn)
        self.initial_layout.addWidget(self.menu_fav_btn)

        self.menu_math_btn.clicked.connect(self.MainMenuButtonClickHandler)
        self.menu_phys_btn.clicked.connect(self.MainMenuButtonClickHandler)
        self.menu_chem_btn.clicked.connect(self.MainMenuButtonClickHandler)
        self.menu_fav_btn.clicked.connect(self.MainMenuButtonClickHandler)

        self.main_menu_widget = QWidget()
        self.main_menu_widget.setLayout(self.initial_layout)
        self.show()

    def MainMenuButtonClickHandler(self):
        """Handles main menu button clicks, directs user to selected submenu"""
        if self.sender() == self.menu_math_btn:
            self.stacked_layout.setCurrentIndex(self.math_menu_stack_position)

        elif self.sender() == self.menu_phys_btn:
            self.stacked_layout.setCurrentIndex(self.phys_menu_stack_position)

        elif self.sender() == self.menu_chem_btn:
            self.stacked_layout.setCurrentIndex(self.chem_menu_stack_position)

        elif self.sender() == self.menu_fav_btn:
            self.stacked_layout.setCurrentIndex(self.fav_menu_stack_position)

    """
        MATH MENU, HELPER CLASSES, AND ASSOCIATED WIDGETS
    """

    def create_math_menu(self):
        """Math Submenu"""
        self.math_menu_stack_position = 1
        # build buttons and labels
        label = QLabel('Math Menu')
        self.widget_btn_add = QPushButton('Add', self)
        self.widget_btn_add.clicked.connect(self.MathMenuButtonClickHandler)
        self.widget_btn_add.setProperty("menuButton", False)
        self.widget_btn_power = QPushButton('Power', self)
        self.widget_btn_power.clicked.connect(self.MathMenuButtonClickHandler)
        self.widget_btn_power.setProperty("menuButton", False)
        self.widget_btn_integral = QPushButton('Integral', self)
        self.widget_btn_integral.clicked.connect(self.MathMenuButtonClickHandler)
        self.widget_btn_integral.setProperty("menuButton", False)
        self.widget_btn_derivative = QPushButton('Derivative', self)
        self.widget_btn_derivative.setProperty("menuButton", False)
        self.widget_btn_RRE = QPushButton('Row-Reduce', self)
        self.widget_btn_RRE.setProperty("menuButton", False)
        self.widget_btn_determinant = QPushButton('Determinant', self)
        self.widget_btn_determinant.setProperty("menuButton", False)
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.backButton(self.main_menu_stack_position))
        back_btn.setProperty("menuButton", True)

        # create layout
        self.math_menu_layout = QGridLayout()
        self.math_menu_layout.addWidget(label, 0 , 0, 1, 1)
        self.math_menu_layout.addWidget(self.widget_btn_add, 1, 0)
        self.math_menu_layout.addWidget(self.widget_btn_power, 1, 1)
        self.math_menu_layout.addWidget(self.widget_btn_integral, 1, 2)
        self.math_menu_layout.addWidget(self.widget_btn_derivative, 1, 3)
        self.math_menu_layout.addWidget(self.widget_btn_RRE, 2, 0)
        self.math_menu_layout.addWidget(self.widget_btn_determinant, 2, 1)
        self.math_menu_layout.addWidget(back_btn, 3, 0, 1, 4)


        # create stack object

        self.math_menu = QWidget()
        self.math_menu.setLayout(self.math_menu_layout)
        self.show()

    def MathMenuButtonClickHandler(self):
        """Handles math submenu button clicks"""
        if self.sender() == self.widget_btn_add:
            self.stacked_layout.setCurrentIndex(self.add_widget_stack_position)
        elif self.sender() == self.widget_btn_power:
            self.stacked_layout.setCurrentIndex(self.power_widget_stack_position)
        elif self.sender() == self.widget_btn_integral:
            self.stacked_layout.setCurrentIndex(self.integral_widget_stack_position)

    def create_add_widget(self):
        """Widget for adding numbers"""
        self.add_widget_stack_position = 5

        # build stack widget
        self.add_widget = QWidget()

        # create inputs buttons and outputs
        input_one_label = QLabel('Input One')
        input_two_label = QLabel('Input Two')
        output_label = QLabel('Sum')
        input_one = QLineEdit()
        input_two = QLineEdit()
        self.add_output = QLineEdit()
        calc_btn = QPushButton('Calculate', self)
        calc_btn.setProperty("menuButton", False)
        calc_btn.clicked.connect(lambda: self.add_widget_calculate(input_one, input_two))
        back_btn = QPushButton('Back', self)
        back_btn.setProperty("menuButton", True)
        back_btn.clicked.connect(lambda: self.backButton(self.math_menu_stack_position))

        # setup gridlayout
        grid = QGridLayout()

        # add widgets to grid
        grid.addWidget(input_one_label, 1, 0)
        grid.addWidget(input_one, 1, 1)
        grid.addWidget(input_two_label, 2, 0)
        grid.addWidget(input_two, 2, 1)
        grid.addWidget(calc_btn, 3, 1, 1, 1)
        grid.addWidget(output_label, 4, 0)
        grid.addWidget(self.add_output, 4, 1)
        grid.addWidget(back_btn, 5, 0, 1,2)

        # create stack object
        self.add_widget.setLayout(grid)
        self.show()

    def add_widget_calculate(self, input_one, input_two):
        """calculates sum for add widget"""
        i_one = input_one.text()
        i_two = input_two.text()

        try:
            in_one = float(i_one)
            in_two = float(i_two)

            out_sum = MathToolWidgets.Add.calc(in_one, in_two)
            self.add_output.setText(str(out_sum))
        except ValueError:
            self.add_output.setText("Please enter a number")

    def create_power_widget(self):
        """Widget for ...."""
        self.power_widget_stack_position = 6  # set stack position, reference attached doc

        # build stack widget
        self.power_widget = QWidget()

        # create inputs, buttons, and outputs
        title = QLabel('Power')
        label_one = QLabel('Base:')
        label_two = QLabel('Power: ')
        input_one = QLineEdit()
        input_two = QLineEdit()
        self.power_output = QLineEdit()
        calc_btn = QPushButton('Calculate', self)
        calc_btn.setProperty("menuButton", False)
        calc_btn.clicked.connect(lambda: self.power_widget_calculate(input_one, input_two))
        result = QLabel('Result')

        # setup gridlayout
        grid = QGridLayout()
        grid.setSpacing(10)

        # add widgets to grid
        grid.addWidget(title, 0, 0)
        grid.addWidget(label_one, 1, 0)
        grid.addWidget(input_one, 1, 1)
        grid.addWidget(label_two, 2, 0)
        grid.addWidget(input_two, 2, 1)
        grid.addWidget(result, 4, 0)
        grid.addWidget(self.power_output, 4, 1)
        grid.addWidget(calc_btn, 3, 1)

        # create back button
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.backButton(self.math_menu_stack_position))  # update menu to return to
        back_btn.setProperty("menuButton", True)
        grid.addWidget(back_btn, 5, 0, 2, 0)

        # create stack object
        self.power_widget.setLayout(grid)
        self.show()

    def power_widget_calculate(self, input_one, input_two):
        i_one = input_one.text()
        i_two = input_two.text()

        try:
            in_one = float(i_one)
            in_two = float(i_two)

            out_sum = MathToolWidgets.Power.calc(in_one, in_two)
            self.power_output.setText(str(out_sum))
        except ValueError:
            self.power_output.setText("Please enter a number")

    def create_integral_widget(self):
        """Widget for calculating definite integrals"""
        self.integral_widget_stack_position = 7  # set stack position, reference attached doc

        # build stack widget
        self.integral_widget = QWidget()

        # create inputs, buttons, and outputs
        title = QLabel('Definite Integral Calculator')
        func_label = QLabel('Function: ')
        upper_label = QLabel('Upper: ')
        lower_label = QLabel('Lower: ')
        result_label = QLabel('Result: ')
        func_input = QLineEdit()
        upper_input = QLineEdit()
        lower_input = QLineEdit()
        self.integral_output = QLineEdit()
        calc_btn = QPushButton('Calculate')
        calc_btn.clicked.connect(lambda: self.integral_widget_calculate(func_input, upper_input, lower_input))
        calc_btn.setProperty("menuButton", False)

        # setup gridlayout
        grid = QGridLayout()

        # add widgets to grid
        grid.addWidget(title, 0,0,1,1)
        grid.addWidget(func_label, 1,0)
        grid.addWidget(func_input, 1,1)
        grid.addWidget(upper_label, 2,0)
        grid.addWidget(upper_input, 2,1)
        grid.addWidget(lower_label, 3,0)
        grid.addWidget(lower_input, 3,1)
        grid.addWidget(calc_btn, 4,1)
        grid.addWidget(result_label, 5,0)
        grid.addWidget(self.integral_output, 5,1)

        # create back button
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.backButton(self.math_menu_stack_position))  # update menu to return to
        back_btn.setProperty("menuButton", True)
        grid.addWidget(back_btn, 6,0,1,2)

        # create stack object
        self.integral_widget.setLayout(grid)
        self.show()

    def integral_widget_calculate(self, func, upper, lower):
        f = func.text()
        u = upper.text()
        l = lower.text()
        try:
            u_float = float(u)
            l_float = float(l)

            result = MathToolWidgets.Integrate.calc(f, l_float, u_float)
            self.integral_output.setText(str(result))
        except ValueError:
            self.integral_output.setText("Please enter a number")

    # TODO: add new widget pages and add to initialization stack

    """
        PHYSICS MENU, HELPER CLASSES, AND WIDGETS
    """

    def create_phys_menu(self):
        """phys Submenu"""
        self.phys_menu_stack_position = 2
        # buttons for physics subwidgets
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.backButton(self.main_menu_stack_position))
        back_btn.setProperty("menuButton", True)
        label = QLabel('Physics')

        # create layout
        self.phys_menu_layout = QVBoxLayout()
        self.phys_menu_layout.addWidget(label)
        self.phys_menu_layout.addWidget(back_btn)

        # create stack object
        self.phys_menu = QWidget()
        self.phys_menu.setLayout(self.phys_menu_layout)
        self.show()

    def PhysMenuButtonClickHandler(self):
        """Handles physics submenu button clicks"""
        if True: # self.sender() == self.widget_btn:
            pass

    """
        CHEMISTRY MENU, HELPER CLASSES, AND WIDGETS
    """

    def create_chem_menu(self):
        """phys Submenu"""
        self.chem_menu_stack_position = 3
        # buttons for physics subwidgets
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.backButton(self.main_menu_stack_position))
        back_btn.setProperty("menuButton", True)
        label = QLabel('Chemistry')

        # create layout
        self.chem_menu_layout = QVBoxLayout()
        self.chem_menu_layout.addWidget(label)
        self.chem_menu_layout.addWidget(back_btn)

        # create stack object
        self.chem_menu = QWidget()
        self.chem_menu.setLayout(self.chem_menu_layout)
        self.show()

    def ChemMenuButtonClickHandler(self):
        """Handles chemistry submenu button clicks"""
        if True: # self.sender() == self.widget_btn:
            pass

    """
        FAVORITES MENU, HELPER CLASSES, AND WIDGETS
    """

    def create_fav_menu(self):
        """phys Submenu"""
        self.fav_menu_stack_position = 4
        # buttons for physics subwidgets
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.backButton(self.main_menu_stack_position))
        back_btn.setProperty("menuButton", True)
        label = QLabel('Favorites')

        # create layout
        self.fav_menu_layout = QVBoxLayout()
        self.fav_menu_layout.addWidget(label)
        self.fav_menu_layout.addWidget(back_btn)

        # create stack object
        self.fav_menu = QWidget()
        self.fav_menu.setLayout(self.fav_menu_layout)
        self.show()

    def FavMenuButtonClickHandler(self):
        """Handles Favorites submenu button clicks"""
        if True: # self.sender() == self.widget_btn:
            pass

    """
        OTHER METHODS
    """

    def backButton(self, index):
        """Goes back in the layout stack"""
        self.stacked_layout.setCurrentIndex(index)

    def create_splash_screen(self):
        """Creates a loading screen"""



if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash_pix = QPixmap('splash_screen.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    left = 100
    top = 100
    width = 900
    height = 750
    splash.setGeometry(left, top, width, height)
    splash.show()
    app.processEvents()
    time.sleep(2)

    m = MainGUI()
    m.show()
    splash.finish(m)
    sys.exit(app.exec_())
