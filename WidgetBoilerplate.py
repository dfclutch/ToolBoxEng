def create_NAME_widget(self):
    """Widget for ...."""
    self.CHANGE_NAME_widget_stack_position = 0  # set stack position, reference attached doc

    # build stack widget
    self.CHANGE_NAME_widget = QWidget()

    # create inputs, buttons, and outputs

    # setup gridlayout
    grid = QGridLayout()
    grid.setSpacing(10)

    # add widgets to grid

    # create back button
    back_btn = QPushButton('Back', self)
    back_btn.clicked.connect(lambda: self.backButton(self.CHANGE_MENU_stack_position))  # update menu to return to
    back_btn.setProperty("menuButton", True)
    fav_btn = QPushButton('Add To Favorites')
    fav_btn.setProperty("menuButton", True)

    # build favorites button for widget
    fav_menu_btn = QPushButton('WIDGET NAME')
    fav_menu_btn.setProperty("menuButton", True)
    fav_menu_btn.clicked.connect(lambda: self.ButtonHandler(self.CHANGE_NAME_widget_stack_position))

    fav_btn.clicked.connect(lambda: self.favButton(fav_menu_btn))
    grid.addWidget(fav_btn)
    grid.addWidget(back_btn)

    # create stack object
    self.CHANGE_NAME_widget.setLayout(grid)
    self.show()
