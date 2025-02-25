from proven.views.menu import MenuView
from proven.views.menu import MenuItem


class MenuOptions(MenuView):
    """
    Main menu implementation with predefined options.
    author: Arnau Núñez López
    grup: DAM2
    """

    def __init__(self):
        """Initialize main menu with default options."""
        super().__init__()
        self.add_item("Exit", "exit", None)
        self.add_item("Option 1", "option1", None)
        self.add_item("Option 2", "option2", None)