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
        self.view.items[1].handler = self._handle_absence_data
        self.view.items[2].handler = self._handle_absence_days
        self.view.items[3].handler = self._handle_save_to_csv
        self.view.items[4].handler = self._handle_calculate_salary

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

    def _handle_absence_data(self) -> None:
        """Handle absence data menu option."""
        departments = input("Enter department you want ('Sales', 'Administration' or 'Purchases'): ")
        if departments not in ["Sales", "Administration", "Purchases"]:
            self.view.display_error("Invalid department")
            return
        absence_status = input("Enter absence status you want (v)validated or (c)confirmed: ")
        if absence_status == "v":
            absence_status = "validate"
        elif absence_status == "c":
            absence_status = "confirm"
        else:
            self.view.display_error("Invalid absence status")
            return
        self.view.display_message("Fetching absence data...")
        try:
            results = self.model.get_table_data(
                "hr_department hd, hr_employee he, hr_leave hl, hr_leave_type hlt",
                "hd.name, he.name, he.work_email, hl.number_of_days, hlt.name, hl.private_name, hl.request_date_to, hl.request_date_from",
                ("hd.id = he.id AND hl.id = hd.id AND hd.id = hlt.id AND hd.name = %s AND hl.state = %s",
                 (departments, absence_status))
            )
            self.view.display_results(results)
        except ModelError as e:
            self.view.display_error(str(e))

    def _handle_absence_days(self) -> None:
        """Handle absence days menu option."""
        self.view.display_message("Fetching employees with absence days greater than 5 days...")
        try:
            results = self.model.execute_query("""
                SELECT hd.name, he.name, hl.number_of_days 
                FROM hr_department hd 
                JOIN hr_employee he ON hd.id = he.department_id 
                JOIN hr_leave hl ON he.id = hl.employee_id 
                WHERE hl.number_of_days > 5
            """
            )
            self.view.display_results(results)
            filename = input("Enter the name of the file you want to save the results to: ")
            self.model.save_results_to_file(results, filename)
            self.view.display_message(f"Results saved to {filename}")
            self.RESULTS_TO_CSV = results
            self.RESULTS_TO_CSV_FILENAME = filename
        except ModelError as e:
            self.view.display_error(str(e))

    def _handle_save_to_csv(self) -> None:
        """Handle save to CSV menu option."""
        if self.RESULTS_TO_CSV is None:
            self.view.display_error("No results to save")
            return
        self.view.display_message("Fetching data to save to CSV...")
        try:
            self.model.save_results_to_csv(self.RESULTS_TO_CSV, self.RESULTS_TO_CSV_FILENAME)
        except ModelError as e:
            self.view.display_error(str(e))

    def _handle_calculate_salary(self) -> None:
        """Handle calculate salary menu option."""
        try:
            hours_dedicated = float(input("Enter the hours: "))
            fee = 360 / (4 * 20)  # 360€ por 4 horas al día durante 20 días
            total_bill = hours_dedicated * fee
            self.view.display_message(f"Hours dedicated: {hours_dedicated}")
            self.view.display_message(f"Total of the bill: {total_bill:.2f}€")
        except ValueError:
            self.view.display_error("Invalid input, please enter a numeric value.")