# src/main.py
from db.initialize import initialize_database
from db.connection import create_connection
from utils.menu import run_menu

def main():
    # Connect DB
    connection = create_connection("../data/inventory.db")

    # Initialize DB
    initialize_database(connection)

    # Run the interactive menu
    run_menu(connection)

if __name__ == "__main__":
    main()