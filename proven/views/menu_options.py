# proven/views/menu_options.py
from proven.views.menu import MenuView


class MenuOptions(MenuView):
    """
    Main menu implementation with predefined options.
    author: Arnau Núñez López
    grup: DAM2
    """

    def __init__(self):
        """Initialize main menu with default options."""
        super().__init__()
        self.add_item("Exit")
        self.add_item("Show sales")
        self.add_item("Show data of a file")
        self.add_item("Save data to file (CSV)")
