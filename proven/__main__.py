# proven/__main__.py
from proven.models.model import Model
from proven.views.menu_options import MenuOptions
from proven.controllers.controller import Controller

def main():
    """
    Main function to initialize and run the application.
    """
    model = Model()
    view = MenuOptions()
    controller = Controller(model, view)
    controller.run()

if __name__ == "__main__":
    main()