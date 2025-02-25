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
            self.control.process_request(None)

    def show_menu(self, title, options):
        """
        Display menu title and options.

        Args:
            title (str): Menu title
            options (list): List of menu options
        """
        print(f"============ {title} ============")
        for idx, option in enumerate(options):
            print(f"[{idx}] {option.text}")

    def display_message(self, message):
        """
        Display a message to the user.

        Args:
            message (str): Message to display
        """
        print(message)

    def display_error(self, error):
        """
        Display an error message.

        Args:
            error (str): Error message to display
        """
        print(f"Error: {error}")

    def display_query_results(self, table_name, results):
        """
        Display query results row by row.

        Args:
            table_name (str): Name of the queried table
            results (list): Query results to display
        """
        print(f"\nQuery results from {table_name}:")
        print("Press Enter to see each result (or 'q' to quit):")
        for row in results:
            user_input = input()
            if user_input.lower() == 'q':
                break
            print(row)

    def display_connection_info(self, dsn):
        """
        Display database connection information.

        Args:
            dsn (str): Database connection string
        """
        print(f"Connected to database: {dsn}")
