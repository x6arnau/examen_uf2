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
    if not model.connect_to_db():
        print("Error connecting to database")
        return
    print("Connected to database: " + model.db.connection.dsn)
    try:
        controller = Controller(model, None)
        menu_view = MenuView(controller, model)
        controller.view = menu_view
        menu_view.display()
    finally:
        model.disconnect_from_db()


if __name__ == "__main__":
    main()
