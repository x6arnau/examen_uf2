# proven/controllers/controller.py
from proven.models.model import ModelError, Model
from proven.views.menu import MenuView


class Controller:
    """
    Main controller class implementing application logic and menu handlers.
    """

    def __init__(self, model: Model, view: MenuView):
        """
        Initialize controller with model and view.

        Args:
            model (Model): Database model instance
            view (MenuView): Menu view instance
        """
        self.model = model
        self.view = view
        self._setup_menu()

    def _setup_menu(self) -> None:
        """Set up menu handlers for each menu item."""
        self.view.items[0].handler = self._handle_exit
        self.view.items[1].handler = self._handle_view_data
        self.view.items[2].handler = self._handle_search

    def run(self) -> None:
        """
        Main application loop handling menu interaction and database connection.
        """
        try:
            if not self.model.connect():
                self.view.display_error("Failed to connect to database")
                return
            self.view.display_message("Connected to database")
            while True:
                self.view.show()
                choice = self.view.get_input()

                if choice == -1:
                    self.view.display_error("Invalid option")
                    continue

                self.view.items[choice].handler()

        except ModelError as e:
            self.view.display_error(str(e))
        finally:
            self.model.disconnect()

    def _handle_exit(self) -> None:
        """Handle exit menu option and cleanup."""
        self.view.display_message("Goodbye!")
        self.model.disconnect()
        self.view.display_message("Disconnected from database")
        exit(0)

    def _handle_view_data(self) -> None:
        """Handle view all data menu option."""
        try:
            results = self.model.get_table_data("table_name")
            self.view.display_results(results)
        except ModelError as e:
            self.view.display_error(str(e))

    def _handle_search(self) -> None:
        """Handle search menu option."""
        try:
            name = input("Enter data to search: ")
            results = self.model.get_table_data(
                "table_name",
                "column1, column2, column3",
                ("column2 LIKE %s", (f"%{name}%",))
            )
            self.view.display_results(results)
        except ModelError as e:
            self.view.display_error(str(e))
