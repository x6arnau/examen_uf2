# proven/views/menu_options.py
from proven.views.menu import Menu
from proven.views.option import Option


class MenuOptions(Menu):
    """
    Main menu implementation with predefined options.
    author: Arnau Núñez López
    grup: DAM2

    Inherits from Menu class and initializes with standard options.
    """

    def __init__(self):
        """Initialize main menu with default options."""
        super().__init__("Main Menu")
        self.add_option(Option("Exit", "exit"))
        self.add_option(Option("Option 1", "option1"))
        self.add_option(Option("Option 2", "option2"))
