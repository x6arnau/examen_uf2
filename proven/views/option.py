# proven/views/option.py
class Option:
    """
    Menu option class representing a single menu choice.
    author: Arnau Núñez López
    grup: DAM2

    Attributes:
        text (str): Display text for the option
        action_command (str): Command associated with the option
    """

    def __init__(self, text, action_command):
        """
        Initialize option with text and command.

        Args:
            text (str): Display text
            action_command (str): Associated command
        """
        self.text = text
        self.action_command = action_command

    def __str__(self):
        """
        String representation of the option.

        Returns:
            str: Formatted string with option details
        """
        return f"Option [text={self.text}, action_command={self.action_command}]"
