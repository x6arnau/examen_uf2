# proven/__main__.py
from models.model import Model
from views.menu_view import MenuView
from controllers.controller import Controller


def main():
    """
    Main application entry point.
    author: Arnau Núñez López
    grup: DAM2

    Initializes MVC components and starts the application.
    """
    model = Model()
    controller = Controller(model, None)
    menu_view = MenuView(controller, model)
    controller.view = menu_view
    model.view = menu_view
    model.db.view = menu_view

    if not model.connect_to_db():
        menu_view.display_error("Error connecting to database")
        return

    menu_view.display_connection_info(model.db.connection.dsn)
    try:
        menu_view.display()
    finally:
        model.disconnect_from_db()


if __name__ == "__main__":
    main()
