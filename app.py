from src.load.db_check import db_operations
from src.load.main import load_and_insert_data


def main():
    try:
        db_operations()
    except Exception as e:
        print(f"Error db_operations: {e}")
        return
    try:
        load_and_insert_data()
    except Exception as e:
        print(f"Error load and insert data: {e}")
        return


if __name__ == "__main__":
    main()
