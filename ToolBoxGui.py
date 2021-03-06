import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import QColor
from PyQt5.QtCore import *
import MathToolWidgets
import PhysicsToolWidgets
import ChemistryToolWidgets
import time
import csv

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
        p.setColor(self.backgroundRole(), QColor('white'))
        self.setPalette(p)

        self.setStyleSheet("""
            QPushButton[menuButton = "true"]{
                border: none;
                border-radius: 10px;
                background-color: #3b77d6;
                font-family: "Helvetica";
                font-size: 34px;
                color: white;
                padding: 10px;
                min-height: 60px;
                align: center;
            }

            QPushButton[menuButton = "false"] {
                border: none;
                border-radius: 8px;
                background-color: #3b77d6;
                font-family: "Helvetica";
                font-size: 28px;
                color: white;
                padding: 8px;      
                min-width: 180px;
                min-height: 180px;

            }

            QPushButton[mainMenuButton = "true"]{
                border: none;
                border-radius: 10px;
                background-color: #3b77d6;
                font-family: "Helvetica";
                font-size: 34px;
                color: white;
                padding: 10px;
                min-height: 100px;
            }

            QPushButton:hover {
                background-color: #2f5faa;
            }

            QPushButton:pressed {
                background-color: #244882;
            }
            
            QMenuBar {
                border: none;
                background-color: #3b77d6;
                font-family: "Helvetica";
                font-size: 34px;
                color: white;
                min-height: 60px;
            }
            
            QMenuBar::item {
                padding: 15px;
                margin: 0px
            }            
            
            QMenuBar::item::selected {
                background-color: #2f5faa;
            }
            
            QMenuBar::item::pressed {
                background-color: #244882;
            }
            
            QLabel {   
                font-family: "Helvetica";
                font-size: 28px;    
                color: black;        
            }
            
            QLabel[description = "true"] {   
                font-family: "Helvetica";
                font-size: 28px;    
                color: #aaaaaa;        
            }

            QWidget {
                padding: 10px;
            }

            QLineEdit {
                font-size: 28px;
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
        self.create_resband_widget()
        self.stacked_layout.addWidget(self.resband_widget)
        self.create_dense_widget()
        self.stacked_layout.addWidget(self.dense_widget)
        self.create_molar_mass_widget()
        self.stacked_layout.addWidget(self.molar_mass_widget)
        self.create_volt_drop_widget()
        self.stacked_layout.addWidget(self.volt_drop_widget)
        self.create_amp_change_widget()
        self.stacked_layout.addWidget(self.amp_change_widget)

        self.stacked_layout.setCurrentIndex(0)

    """
        MAIN MENU AND MAIN MENU HELPER CLASSES
    """

    def create_main_menu_layout(self):
        """Creates main menu"""
        # general properties #
        self.main_menu_stack_position = 0
        self.main_menu_widget = QWidget()

        # create menus #
        menu_bar = self.menuBar()
        math_menu = menu_bar.addMenu('Math')
        phys_menu = menu_bar.addMenu('Physics')
        chem_menu = menu_bar.addMenu('Chemistry')
        fav_menu = menu_bar.addMenu('Favorites')

        # create add menu #
        math_menu_action = QAction('Menu', self)
        math_menu_action.triggered.connect(lambda: self.ButtonHandler(self.math_menu_stack_position))
        math_menu.addAction(math_menu_action)
        add_action = QAction('Add', self)
        add_action.triggered.connect(lambda: self.ButtonHandler(self.add_widget_stack_position))
        math_menu.addAction(add_action)
        power_action = QAction('Power', self)
        power_action.triggered.connect(lambda: self.ButtonHandler(self.power_widget_stack_position))
        math_menu.addAction(power_action)
        integral_action = QAction('Integral', self)
        integral_action.triggered.connect(lambda: self.ButtonHandler(self.integral_widget_stack_position))
        math_menu.addAction(integral_action)

        # create physics menu #
        phys_menu_action = QAction('Menu', self)
        phys_menu_action.triggered.connect(lambda: self.ButtonHandler(self.phys_menu_stack_position))
        phys_menu.addAction(phys_menu_action)
        resband_action = QAction('Resistor Bands', self)
        resband_action.triggered.connect(lambda: self.ButtonHandler(self.resband_widget_stack_position))
        phys_menu.addAction(resband_action)
        dense_action = QAction('Material Density', self)
        dense_action.triggered.connect(lambda: self.ButtonHandler(self.dense_widget_stack_position))
        phys_menu.addAction(dense_action)
        volt_action = QAction('Voltage Drop', self)
        volt_action.triggered.connect(lambda: self.ButtonHandler(self.volt_drop_widget_stack_position))
        phys_menu.addAction(volt_action)
        amp_change = QAction('Amp Change', self)
        amp_change.triggered.connect(lambda: self.ButtonHandler(self.amp_change_widget_stack_position))
        phys_menu.addAction(amp_change)

        # create chem menu #
        chem_menu_action = QAction('Menu', self)
        chem_menu_action.triggered.connect(lambda: self.ButtonHandler(self.chem_menu_stack_position))
        chem_menu.addAction(chem_menu_action)
        molar_action = QAction('Molar Mass', self)
        molar_action.triggered.connect(lambda: self.ButtonHandler(self.molar_mass_widget_stack_position))
        chem_menu.addAction(molar_action)

        # create favorites menu #
        fav_menu_action = QAction('Menu', self)
        fav_menu_action.triggered.connect(lambda: self.ButtonHandler(self.fav_menu_stack_position))
        fav_menu.addAction(fav_menu_action)
        fav_menu.triggered.connect(lambda: self.ButtonHandler(self.fav_menu_stack_position))

        self.show()
    """
        MATH MENU, HELPER CLASSES, AND ASSOCIATED WIDGETS
    """

    def create_math_menu(self):
        """Math Submenu"""
        self.math_menu_stack_position = 1
        # build buttons and labels
        self.widget_btn_add = QPushButton('Add', self)
        self.widget_btn_add.clicked.connect(lambda: self.ButtonHandler(self.add_widget_stack_position))
        self.widget_btn_add.setProperty("menuButton", False)
        self.widget_btn_power = QPushButton('Power', self)
        self.widget_btn_power.clicked.connect(lambda: self.ButtonHandler(self.power_widget_stack_position))
        self.widget_btn_power.setProperty("menuButton", False)
        self.widget_btn_integral = QPushButton('Definite\nIntegral', self)
        self.widget_btn_integral.clicked.connect(lambda: self.ButtonHandler(self.integral_widget_stack_position))
        self.widget_btn_integral.setProperty("menuButton", False)
        self.widget_btn_derivative = QPushButton('Derivative', self)
        self.widget_btn_derivative.setProperty("menuButton", False)
        self.widget_btn_RRE = QPushButton('Row-Reduce', self)
        self.widget_btn_RRE.setProperty("menuButton", False)
        self.widget_btn_determinant = QPushButton('Determinant', self)
        self.widget_btn_determinant.setProperty("menuButton", False)
        # create layout
        self.math_menu_layout = QVBoxLayout()
        self.math_menu_grid_layout = QGridLayout()
        self.math_menu_grid_layout.addWidget(self.widget_btn_add, 1, 0)
        self.math_menu_grid_layout.addWidget(self.widget_btn_power, 1, 1)
        self.math_menu_grid_layout.addWidget(self.widget_btn_integral, 1, 2)
        self.math_menu_grid_layout.addWidget(self.widget_btn_derivative, 1, 3)
        self.math_menu_grid_layout.addWidget(self.widget_btn_RRE, 2, 0)
        self.math_menu_grid_layout.addWidget(self.widget_btn_determinant, 2, 1)
        self.math_menu_layout.addLayout(self.math_menu_grid_layout)

        # create stack object

        self.math_menu = QWidget()
        self.math_menu.setLayout(self.math_menu_layout)
        self.show()

    def create_add_widget(self):
        """Widget for adding numbers"""
        # widget attributes
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
        calc_btn.setProperty("menuButton", True)
        calc_btn.clicked.connect(lambda: self.add_widget_calculate(input_one, input_two))
        back_btn = QPushButton('Back', self)
        back_btn.setProperty("menuButton", True)
        back_btn.clicked.connect(lambda: self.ButtonHandler(self.math_menu_stack_position))
        fav_btn = QPushButton('Add To Favorites')
        fav_btn.setProperty("menuButton", True)

        # build favorites button for widget
        fav_menu_btn = QPushButton('Add')
        fav_menu_btn.setProperty("menuButton", True)
        fav_menu_btn.clicked.connect(lambda: self.ButtonHandler(self.add_widget_stack_position))

        fav_btn.clicked.connect(lambda: self.favButton(fav_menu_btn))

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
        grid.addWidget(back_btn, 5, 1, 1, 1)
        grid.addWidget(fav_btn, 5, 0, 1, 1)

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
        """Widget for raising a base to a power"""
        self.power_widget_stack_position = 6  # set stack position, reference attached doc

        # build stack widget
        self.power_widget = QWidget()

        # create inputs, buttons, and outputs
        label_one = QLabel('Base:')
        label_two = QLabel('Power: ')
        input_one = QLineEdit()
        input_two = QLineEdit()
        self.power_output = QLineEdit()
        calc_btn = QPushButton('Calculate', self)
        calc_btn.setProperty("menuButton", True)
        calc_btn.clicked.connect(lambda: self.power_widget_calculate(input_one, input_two))
        result = QLabel('Result')
        fav_btn = QPushButton('Add To Favorites')
        fav_btn.setProperty("menuButton", True)

        # build favorites button for widget
        fav_menu_btn = QPushButton('Power')
        fav_menu_btn.setProperty("menuButton", True)
        fav_menu_btn.clicked.connect(lambda: self.ButtonHandler(self.power_widget_stack_position))

        fav_btn.clicked.connect(lambda: self.favButton(fav_menu_btn))

        # setup gridlayout
        grid = QGridLayout()
        grid.setSpacing(10)

        # add widgets to grid
        grid.addWidget(label_one, 1, 0)
        grid.addWidget(input_one, 1, 1)
        grid.addWidget(label_two, 2, 0)
        grid.addWidget(input_two, 2, 1)
        grid.addWidget(result, 4, 0)
        grid.addWidget(self.power_output, 4, 1)
        grid.addWidget(calc_btn, 3, 1, 1, 1)

        # create back button
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.ButtonHandler(self.math_menu_stack_position))  # update menu to return to
        back_btn.setProperty("menuButton", True)
        grid.addWidget(fav_btn, 5, 0, 1, 1)
        grid.addWidget(back_btn, 5, 1, 1, 1)

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
        calc_btn.setProperty("menuButton", True)

        # setup gridlayout
        grid = QGridLayout()

        # add widgets to grid
        grid.addWidget(func_label, 1, 0)
        grid.addWidget(func_input, 1, 1)
        grid.addWidget(upper_label, 2, 0)
        grid.addWidget(upper_input, 2, 1)
        grid.addWidget(lower_label, 3, 0)
        grid.addWidget(lower_input, 3, 1)
        grid.addWidget(calc_btn, 4, 1)
        grid.addWidget(result_label, 5, 0)
        grid.addWidget(self.integral_output, 5, 1)
        fav_btn = QPushButton('Add To Favorites')
        fav_btn.setProperty("menuButton", True)

        # build favorites button for widget
        fav_menu_btn = QPushButton('Integral')
        fav_menu_btn.setProperty("menuButton", True)
        fav_menu_btn.clicked.connect(lambda: self.ButtonHandler(self.integral_widget_stack_position))

        fav_btn.clicked.connect(lambda: self.favButton(fav_menu_btn))

        # create back button
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.ButtonHandler(self.math_menu_stack_position))  # update menu to return to
        back_btn.setProperty("menuButton", True)
        grid.addWidget(fav_btn, 6, 0, 1, 1)
        grid.addWidget(back_btn, 6, 1, 1, 1)

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

    """
        PHYSICS MENU, HELPER CLASSES, AND WIDGETS
    """

    def create_phys_menu(self):
        """phys Submenu"""
        self.phys_menu_stack_position = 2
        # buttons for physics subwidgets
        self.widget_btn_resband = QPushButton('Resistor\nBands')
        self.widget_btn_resband.setProperty("menuButton", False)
        self.widget_btn_resband.clicked.connect(lambda: self.ButtonHandler(self.resband_widget_stack_position))
        self.widget_btn_dense = QPushButton('Material\nDensities')
        self.widget_btn_dense.setProperty("menuButton", False)
        self.widget_btn_dense.clicked.connect(lambda: self.ButtonHandler(self.dense_widget_stack_position))
        self.widget_btn_volt = QPushButton('Voltage\nDrop')
        self.widget_btn_volt.setProperty("menuButton", False)
        self.widget_btn_volt.clicked.connect(lambda: self.ButtonHandler(self.volt_drop_widget_stack_position))
        self.widget_btn_amp_change = QPushButton('Amp Change')
        self.widget_btn_amp_change.setProperty("menuButton", False)
        self.widget_btn_amp_change.clicked.connect(lambda: self.ButtonHandler(self.amp_change_widget_stack_position))


        # create layout
        self.phys_menu_layout = QVBoxLayout()
        self.phys_widget_layout = QGridLayout()
        self.phys_widget_layout.addWidget(self.widget_btn_resband, 0, 0, 1, 1)
        self.phys_widget_layout.addWidget(self.widget_btn_dense, 0, 1, 1, 1)
        self.phys_widget_layout.addWidget(self.widget_btn_volt, 0, 2, 1, 1)
        self.phys_widget_layout.addWidget(self.widget_btn_amp_change, 0, 3, 1, 1)

        self.phys_menu_layout.addLayout(self.phys_widget_layout)

        # create stack object
        self.phys_menu = QWidget()
        self.phys_menu.setLayout(self.phys_menu_layout)
        self.show()

    def create_resband_widget(self):
        """Widget for Calculating resistor values"""
        self.resband_widget_stack_position = 8  # set stack position, reference attached doc

        # build stack widget
        self.resband_widget = QWidget()

        # create inputs, buttons, and outputs
        label_one = QLabel('1st Band: ')
        label_two = QLabel('2nd Band: ')
        label_mult = QLabel('Multiplier: ')
        label_tolerance = QLabel('Tolerance: ')
        label_value = QLabel('Value: ')
        band_one = QComboBox()
        band_one.addItems(
            ['Black 0', 'Brown 1', 'Red 2', 'Orange 3', 'Yellow 4', 'Green 5', 'Blue 6', 'Violet 7', 'Gray 8',
             'White 9'])
        band_two = QComboBox()
        band_two.addItems(
            ['Black 0', 'Brown 1', 'Red 2', 'Orange 3', 'Yellow 4', 'Green 5', 'Blue 6', 'Violet 7', 'Gray 8',
             'White 9'])
        band_mult = QComboBox()
        band_mult.addItems(['Black x1 Ω', 'Brown  x10 Ω', 'Red  x100 Ω', 'Orange x1 kΩ', 'Yellow x10 kΩ',
                            'Green x100 kΩ', 'Blue x1 MΩ', 'Violet x10 MΩ', 'Gray x100 MΩ', 'White x1 GΩ',
                            'Gold x.1 Ω', 'Silver x.01 Ω'])
        band_tol = QComboBox()
        band_tol.addItems(['Brown  ±1%', 'Red   ±2%', 'Green ±0.5%', 'Blue ±0.25%', 'Violet ±0.1%', 'Gray ±0.05%',
                           'Gold ±1%', 'Silver ±10%'])
        calc_btn = QPushButton('Calculate')
        calc_btn.setProperty("menuButton", True)
        calc_btn.clicked.connect(lambda: self.resband_calculate(band_one, band_two, band_mult, band_tol))
        self.resband_output = QLineEdit()

        # setup gridlayout
        grid = QGridLayout()

        # add widgets to grid
        grid.addWidget(label_one, 1, 0)
        grid.addWidget(band_one, 1, 1)
        grid.addWidget(label_two, 2, 0)
        grid.addWidget(band_two, 2, 1)
        grid.addWidget(label_mult, 3, 0)
        grid.addWidget(band_mult, 3, 1)
        grid.addWidget(label_tolerance, 4, 0)
        grid.addWidget(band_tol, 4, 1)
        grid.addWidget(calc_btn, 5, 1)
        grid.addWidget(label_value, 6, 0)
        grid.addWidget(self.resband_output, 6, 1)

        # create back and favorite button
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.ButtonHandler(self.phys_menu_stack_position))  # update menu to return to
        back_btn.setProperty("menuButton", True)
        fav_btn = QPushButton('Add To Favorites')
        fav_btn.setProperty("menuButton", True)

        # build favorites button for widget
        fav_menu_btn = QPushButton('Resistor Bands')
        fav_menu_btn.setProperty("menuButton", True)
        fav_menu_btn.clicked.connect(lambda: self.ButtonHandler(self.resband_widget_stack_position))

        fav_btn.clicked.connect(lambda: self.favButton(fav_menu_btn))
        grid.addWidget(fav_btn, 7, 0)
        grid.addWidget(back_btn, 7, 1)

        # create stack object
        self.resband_widget.setLayout(grid)
        self.show()

    def resband_calculate(self, one, two, mult, tol):
        try:
            result = PhysicsToolWidgets.ResistorBand.calc(str(one.currentText()), str(two.currentText()),
                                                          str(mult.currentText()), str(tol.currentText()))
            self.resband_output.setText(result)
        except:
            self.resband_output.setText("Improper Input")

    def create_dense_widget(self):
        """Widget for ...."""
        self.dense_widget_stack_position = 9  # set stack position, reference attached doc

        # build stack widget
        self.dense_widget = QWidget()

        # create inputs, buttons, and outputs
        label_input = QLabel('Material: ')
        label_metr = QLabel('Grams / cm³')
        label_imp = QLabel('Pounds / ft³')
        mat = QComboBox()

        with open('Density01.csv') as csvfile:
            dense = csv.reader(csvfile, delimiter=",")
            mats = []
            self.metr = {}
            self.imp = {}
            for row in dense:
                mats.append(row[0])
                self.metr[row[0]] = row[1]
                self.imp[row[0]] = row[2]

        mat.addItems(mats)

        self.dense_out_metr = QLineEdit()
        self.dense_out_imp = QLineEdit()
        calc_btn = QPushButton('Calculate')
        calc_btn.setProperty("menuButton", True)
        calc_btn.clicked.connect(lambda: self.dense_calculate(str(mat.currentText())))

        # setup gridlayout
        grid = QGridLayout()
        grid.setSpacing(10)

        # add widgets to grid
        grid.addWidget(label_input, 1, 0)
        grid.addWidget(mat, 1, 1)
        grid.addWidget(calc_btn, 2, 1)
        grid.addWidget(label_metr, 3, 0)
        grid.addWidget(self.dense_out_metr, 3, 1)
        grid.addWidget(label_imp, 4, 0)
        grid.addWidget(self.dense_out_imp, 4, 1)

        # create back button
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.ButtonHandler(self.phys_menu_stack_position))  # update menu to return to
        back_btn.setProperty("menuButton", True)
        fav_btn = QPushButton('Add To Favorites')
        fav_btn.setProperty("menuButton", True)

        # build favorites button for widget
        fav_menu_btn = QPushButton('Material Densities')
        fav_menu_btn.setProperty("menuButton", True)
        fav_menu_btn.clicked.connect(lambda: self.ButtonHandler(self.dense_widget_stack_position))

        fav_btn.clicked.connect(lambda: self.favButton(fav_menu_btn))
        grid.addWidget(fav_btn, 5, 0)
        grid.addWidget(back_btn, 5, 1)

        # create stack object
        self.dense_widget.setLayout(grid)
        self.show()

    def dense_calculate(self, material):
        try:
            metr_dense = self.metr.get(material)
            imp_dense = self.imp.get(material)

            self.dense_out_metr.setText(metr_dense)
            self.dense_out_imp.setText(imp_dense)
        except:
            self.dense_out_metr.setText("Something's Not Right!?")

    def create_volt_drop_widget(self):
        """Widget for calculating voltage drop across a resistor"""
        self.volt_drop_widget_stack_position = 11  # set stack position, reference attached doc

        # build stack widget
        self.volt_drop_widget = QWidget()

        # create inputs, buttons, and outputs
        label_voltage = QLabel('Power source: ')
        label_resist = QLabel('Resistor voltage: \ne.g. [22, 18, 44]')
        label_result = QLabel('Drops: ')
        input_voltage = QLineEdit()
        input_resist = QLineEdit()
        self.output_volt_drop = QLineEdit()
        btn_calc = QPushButton('Calculate')
        btn_calc.setProperty("menuButton", True)
        btn_calc.clicked.connect(lambda: self.volt_drop_calculate(input_voltage.text(), input_resist.text()))

        # setup gridlayout
        grid = QGridLayout()

        # add widgets to grid
        grid.addWidget(label_voltage, 0, 0)
        grid.addWidget(input_voltage, 0, 1)
        grid.addWidget(label_resist, 1, 0)
        grid.addWidget(input_resist, 1, 1,)
        grid.addWidget(btn_calc, 2, 1)
        grid.addWidget(label_result, 3, 0)
        grid.addWidget(self.output_volt_drop)

        # create back button
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.ButtonHandler(self.phys_menu_stack_position))  # update menu to return to
        back_btn.setProperty("menuButton", True)
        fav_btn = QPushButton('Add To Favorites')
        fav_btn.setProperty("menuButton", True)

        # build favorites button for widget
        fav_menu_btn = QPushButton('Voltage Drop')
        fav_menu_btn.setProperty("menuButton", True)
        fav_menu_btn.clicked.connect(lambda: self.ButtonHandler(self.volt_drop_widget_stack_position))

        fav_btn.clicked.connect(lambda: self.favButton(fav_menu_btn))
        grid.addWidget(fav_btn, 4, 0)
        grid.addWidget(back_btn, 4, 1)

        # create stack object
        self.volt_drop_widget.setLayout(grid)
        self.show()

    def volt_drop_calculate(self, volt, resist):
        try:
            result = PhysicsToolWidgets.VoltageDrop.calc(volt, resist)
            output = ""
            for x in result:
                output = output + " " + x + " " + result.get(x) + ","

            self.output_volt_drop.setText(output)
        except:
            self.output_volt_drop.setText("mistakes were made")

    def create_amp_change_widget(self):
        """Widget for calculating voltage drop across a resistor"""
        self.amp_change_widget_stack_position = 12  # set stack position, reference attached doc

        # build stack widget
        self.amp_change_widget = QWidget()

        # create inputs, buttons, and outputs
        label_voltage = QLabel('Power source: ')
        label_resist = QLabel('Resistor voltage: \ne.g. [22, 18, 44]')
        label_result = QLabel('Drops: ')
        input_voltage = QLineEdit()
        input_resist = QLineEdit()
        self.output_amp_change = QLineEdit()
        btn_calc = QPushButton('Calculate')
        btn_calc.setProperty("menuButton", True)
        btn_calc.clicked.connect(lambda: self.amp_change_calculate(input_voltage.text(), input_resist.text()))

        # setup gridlayout
        grid = QGridLayout()

        # add widgets to grid
        grid.addWidget(label_voltage, 0, 0)
        grid.addWidget(input_voltage, 0, 1)
        grid.addWidget(label_resist, 1, 0)
        grid.addWidget(input_resist, 1, 1,)
        grid.addWidget(btn_calc, 2, 1)
        grid.addWidget(label_result, 3, 0)
        grid.addWidget(self.output_amp_change)

        # create back button
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.ButtonHandler(self.phys_menu_stack_position))  # update menu to return to
        back_btn.setProperty("menuButton", True)
        fav_btn = QPushButton('Add To Favorites')
        fav_btn.setProperty("menuButton", True)

        # build favorites button for widget
        fav_menu_btn = QPushButton('Amp Change')
        fav_menu_btn.setProperty("menuButton", True)
        fav_menu_btn.clicked.connect(lambda: self.ButtonHandler(self.amp_change_widget_stack_position))

        fav_btn.clicked.connect(lambda: self.favButton(fav_menu_btn))
        grid.addWidget(fav_btn, 4, 0)
        grid.addWidget(back_btn, 4, 1)

        # create stack object
        self.amp_change_widget.setLayout(grid)
        self.show()

    def amp_change_calculate(self, volt, resist):
        try:
            result = PhysicsToolWidgets.AmpChange.calc(volt, resist)
            output = ""
            for x in result:
                output = output + " " + x + " " + result.get(x) + ","

            self.output_amp_change.setText(output)
        except:
            self.output_amp_change.setText("mistakes were made")

    """
        CHEMISTRY MENU, HELPER CLASSES, AND WIDGETS
    """

    def create_chem_menu(self):
        """chem Submenu"""
        self.chem_menu_stack_position = 3

        # buttons for chem subwidgets
        self.widget_btn_molar = QPushButton('Molar Mass')
        self.widget_btn_molar.setProperty("menuButton", False)
        self.widget_btn_molar.clicked.connect(lambda: self.ButtonHandler(self.molar_mass_widget_stack_position))

        # create layout
        self.chem_menu_layout = QVBoxLayout()
        self.chem_widgets_layout = QGridLayout()
        self.chem_widgets_layout.addWidget(self.widget_btn_molar, 0, 0)
        self.chem_menu_layout.addLayout(self.chem_widgets_layout)

        # create stack object
        self.chem_menu = QWidget()
        self.chem_menu.setLayout(self.chem_menu_layout)
        self.show()

    def create_molar_mass_widget(self):
        """Widget for calculating molar mass of a compound"""
        self.molar_mass_widget_stack_position = 10  # set stack position, reference attached doc

        # build stack widget
        self.molar_mass_widget = QWidget()

        # create inputs, buttons, and outputs
        label_input = QLabel('Formula')
        form_input = QLineEdit()
        calc_btn = QPushButton('Calculate')
        calc_btn.setProperty("menuButton", True)
        calc_btn.clicked.connect(lambda: self.molar_mass_calculate(form_input.text()))
        label_output = QLabel('Molar Mass')
        self.molar_mass_out = QLineEdit()

        # setup gridlayout
        grid = QGridLayout()
        grid.setSpacing(10)

        # add widgets to grid
        grid.addWidget(label_input, 1, 0)
        grid.addWidget(form_input, 1, 1)
        grid.addWidget(calc_btn, 2, 1)
        grid.addWidget(label_output, 3, 0)
        grid.addWidget(self.molar_mass_out, 3, 1)

        # create back button
        back_btn = QPushButton('Back', self)
        back_btn.clicked.connect(lambda: self.ButtonHandler(self.chem_menu_stack_position))  # update menu to return to
        back_btn.setProperty("menuButton", True)
        fav_btn = QPushButton('Add To Favorites')
        fav_btn.setProperty("menuButton", True)

        # build favorites button for widget
        fav_menu_btn = QPushButton('Molar Mass')
        fav_menu_btn.setProperty("menuButton", True)
        fav_menu_btn.clicked.connect(lambda: self.ButtonHandler(self.molar_mass_widget_stack_position))

        fav_btn.clicked.connect(lambda: self.favButton(fav_menu_btn))
        grid.addWidget(fav_btn, 4, 0)
        grid.addWidget(back_btn, 4, 1)

        # create stack object
        self.molar_mass_widget.setLayout(grid)
        self.show()

    def molar_mass_calculate(self, formula):
        try:
            result = ChemistryToolWidgets.AtomicMass.calc(str(formula))
            self.molar_mass_out.setText(str(result))
        except:
            self.molar_mass_out.setText("Something's Not Right!?")

    """
        FAVORITES MENU, HELPER CLASSES, AND WIDGETS
    """

    def create_fav_menu(self):
        """fav Submenu"""
        self.fav_menu_stack_position = 4
        # buttons for physics subwidgets

        # create layouts
        self.fav_menu_layout = QVBoxLayout()
        self.fav_btns_layout = QVBoxLayout()

        self.fav_menu_layout.addLayout(self.fav_btns_layout)


        # create stack object
        self.fav_menu = QWidget()
        self.fav_menu.setLayout(self.fav_menu_layout)
        self.show()

    """
        OTHER METHODS
    """

    def favButton(self, button):
        self.fav_btns_layout.addWidget(button)

    def ButtonHandler(self, sp):
        self.stacked_layout.setCurrentIndex(sp)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    left = 100
    top = 100
    width = 900
    height = 750

    splash_pix = QPixmap('splash_screen.png')
    scaled = splash_pix.scaled(width, height, Qt.IgnoreAspectRatio, Qt.FastTransformation)
    splash = QSplashScreen(scaled, Qt.WindowStaysOnTopHint)
    splash.setMask(scaled.mask())

    splash.setGeometry(left, top, width, height)

    splash.show()
    app.processEvents()
    m = MainGUI()
    time.sleep(2)
    m.show()
    splash.finish(m)
    sys.exit(app.exec_())
