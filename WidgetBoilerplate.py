def create_add_widget(self):
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
    back_btn.clicked.connect(lambda: self.backButton(self.menu_stack_position))  # update menu to return to
    grid.addWidget(back_btn)

    # create stack object
    self.CHANGE_NAME_widget.setLayout(grid)
    self.show()