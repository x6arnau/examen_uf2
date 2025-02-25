from proven.models.model import Model
from proven.views.menu_options import MenuOptions
from proven.controllers.controller import Controller


def main():
    model = Model()
    view = MenuOptions()
    controller = Controller(model, view)
    controller.run()


if __name__ == "__main__":
    main()