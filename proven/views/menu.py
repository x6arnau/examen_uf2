# proven/views/menu.py
from dataclasses import dataclass
from typing import List, Callable, Tuple


@dataclass
class MenuItem:
    """
    Represents a menu item with text, command, and associated handler.
    author: Arnau Núñez López
    grup: DAM2

    Attributes:
        text (str): Display text for the menu item
    """
    text: str


class MenuView:
    """
    Base class for menu views implementing common menu functionality.
    """

    def __init__(self):
        """Initialize an empty menu items list."""
        self.items: List[MenuItem] = []

    def add_item(self, text: str) -> None:
        """
        Add a new menu item to the menu.

        Args:
            text (str): Display text for the menu item
        """
        self.items.append(MenuItem(text))

    def show(self) -> None:
        """Display all menu items with their index numbers."""
        print("\n=== Menu ===")
        for idx, item in enumerate(self.items):
            print(f"[{idx}] {item.text}")

    def get_input(self) -> int:
        """
        Get user input for menu selection.

        Returns:
            int: Selected menu index or -1 if invalid input
        """
        try:
            choice = int(input("\nSelect option: "))
            if 0 <= choice < len(self.items):
                return choice
            raise ValueError()
        except ValueError:
            return -1

    def display_message(self, message: str) -> None:
        """
        Display a message to the user.

        Args:
            message (str): Message to display
        """
        print(message)

    def display_error(self, error: str) -> None:
        """
        Display an error message to the user.

        Args:
            error (str): Error message to display
        """
        print(f"Error: {error}")

    def display_results(self, results: List[Tuple]) -> None:
        """
        Display query results with pagination.

        Args:
            results (List[Tuple]): Database query results to display
        """
        if not results:
            print("No results found.")
            return

        print("\nResults:")
        for row in results:
            print(row)
            if input("Press Enter to continue (q to quit): ").lower() == 'q':
                break
