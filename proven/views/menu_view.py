# proven/views/menu_view.py
from proven.views.menu_options import MenuOptions

class MenuView:
    """
    View class handling menu display and user interaction.
    author: Arnau Núñez López
    grup: DAM2

    Attributes:
        control: Controller instance
        menu: MenuOptions instance
    """

    def __init__(self, control, model):
        """
        Initialize view with controller and menu.

        Args:
            control: Controller instance
            model: Model instance
        """
        self.control = control
        self.menu = MenuOptions()

    def display(self):
        """
        Display menu and process user input in a loop.

        Continues until exit option is selected.
        """
        while True:
            self.menu.show()
            action = self.menu.get_selected_option()
            self.process_action(action)

    def process_action(self, action):
        """
        Process selected menu option.

        Args:
            action (int): Selected option index
        """
        if action == 0:
            self.control.process_request("exit")
        elif action == 1:
            self.control.process_request("option1")
        elif action == 2:
            self.control.process_request("option2")
        else:
            print("Invalid option")