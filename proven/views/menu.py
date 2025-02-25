# proven/views/menu.py
class Menu:
    """
    Base menu class for displaying options and handling user input.
    author: Arnau Núñez López
    grup: DAM2

    Attributes:
        title (str): Menu title
        options (list): List of menu options
        view: View instance for displaying output
    """

    def __init__(self, title=None):
        """
        Initialize menu with optional title.

        Args:
            title (str, optional): Menu title. Defaults to None.
        """
        self.title = title
        self.options = []
        self.view = None

    def add_option(self, option):
        """
        Add new option to menu.

        Args:
            option (Option): Option instance to add
        """
        self.options.append(option)

    def show(self):
        """Display menu title and numbered options."""
        if hasattr(self, 'view'):
            self.view.show_menu(self.title, self.options)

    def get_selected_option(self):
        """
        Get user input for option selection.

        Returns:
            int: Selected option index or -1 if invalid
        """
        try:
            option = int(input("Select an option: "))
            if 0 <= option < len(self.options):
                return option
            return -1
        except ValueError:
            return -1
