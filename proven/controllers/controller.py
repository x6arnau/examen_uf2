# proven/controllers/controller.py
from proven.models.model import ModelError, Model
from proven.views.menu import MenuView


class Controller:
    """
    Main controller class implementing application logic and menu handlers.
    author: Arnau Núñez López
    grup: DAM2
    """

    # Stores the results to be saved to a CSV file
    RESULTS_TO_CSV_DATA = None

    # Default filename for saving results to a CSV file
    RESULTS_TO_CSV_FILENAME = "results.csv"

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
        self.view.items[1].handler = self._handle_show_sales
        self.view.items[2].handler = self._handle_show_data_file
        self.view.items[3].handler = self._handle_save_to_csv

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

    def _handle_save_to_csv(self) -> None:
        """Handle save to CSV menu option."""
        if self.RESULTS_TO_CSV_DATA is None:
            self.view.display_error("No results to save")
            return
        self.view.display_message("Fetching data to save to CSV...")
        try:
            self.model.save_results_to_csv(self.RESULTS_TO_CSV_DATA, self.RESULTS_TO_CSV_FILENAME)
        except ModelError as e:
            self.view.display_error(str(e))

    def _handle_show_sales(self) -> None:
        """Handle show sales menu option."""
        try:
            self.view.display_message("Filter to search the sale: client(cl), product(p), comercial(co)")
            filter = input("Select how you wanna search the sale: ")
            if filter not in ["cl", "p", "co"]:
                self.view.display_error("Invalid filter")
                return
            condition = input("Enter name: ")
            self.view.display_message("Fetching from odoo the sale...")
            if filter == "cl":
                results = self.model.get_table_data(
                    "product_product pp "
                    "JOIN public.product_template pt ON pp.product_tmpl_id = pt.id "
                    "JOIN public.res_partner rp ON pp.id = rp.id "
                    "JOIN public.res_users ru ON pp.create_uid = ru.id "
                    "JOIN public.sale_order so ON pp.id = so.id",
                    "pt.name as nom_producte, rp.name as client, ru.login as nom_comercial, so.date_order as data",
                    ("rp.name = %s", (condition,))
                )
                self.view.display_results(results)
                filename = input("Enter the name of the file you want to save the results to: ")
                self.model.save_results_to_file(results, filename)
                self.view.display_message(f"Results saved to {filename}")
                self.RESULTS_TO_CSV_FILENAME = filename
                self.RESULTS_TO_CSV_DATA = results
            elif filter == "p":
                results = self.model.get_table_data(
                    "product_product pp "
                    "JOIN public.product_template pt ON pp.product_tmpl_id = pt.id "
                    "JOIN public.res_partner rp ON pp.id = rp.id "
                    "JOIN public.res_users ru ON pp.create_uid = ru.id "
                    "JOIN public.sale_order so ON pp.id = so.id",
                    "pt.name as nom_producte, rp.name as client, ru.login as nom_comercial, so.date_order as data",
                    ("pt.name = %s", (condition,))
                )
                self.view.display_results(results)
                filename = input("Enter the name of the file you want to save the results to: ")
                self.model.save_results_to_file(results, filename)
                self.view.display_message(f"Results saved to {filename}")
                self.RESULTS_TO_CSV_FILENAME = filename
                self.RESULTS_TO_CSV_DATA = results

            elif filter == "co":
                results = self.model.get_table_data(
                    "product_product pp "
                    "JOIN public.product_template pt ON pp.product_tmpl_id = pt.id "
                    "JOIN public.res_partner rp ON pp.id = rp.id "
                    "JOIN public.res_users ru ON pp.create_uid = ru.id "
                    "JOIN public.sale_order so ON pp.id = so.id",
                    "pt.name as nom_producte, rp.name as client, ru.login as nom_comercial, so.date_order as data",
                    ("ru.login = %s", (condition,))
                )
                self.view.display_results(results)
                filename = input("Enter the name of the file you want to save the results to: ")
                self.model.save_results_to_file(results, filename)
                self.view.display_message(f"Results saved to {filename}")
                self.RESULTS_TO_CSV_FILENAME = filename
                self.RESULTS_TO_CSV_DATA = results
            else:
                self.view.display_message("Error at the filter")
        except ModelError as e:
            self.view.display_error(str(e))

    def _handle_show_data_file (self) -> None:
        """Handle show data of a file menu option."""
        # TODO