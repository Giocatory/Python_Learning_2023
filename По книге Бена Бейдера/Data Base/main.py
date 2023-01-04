import sqlite3


def main():
    create_table = """CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
    INSERT INTO People VALUES("Mikhail", "Derkunov", 34);"""

    # test_database.db создастся, если его нет
    with sqlite3.connect("test_database.db") as connection:
        cursor = connection.cursor()
        query = "SELECT datetime('now', 'localtime');"
        result = cursor.execute(query)
        row = result.fetchone()
        time = row[0]
        print(time)  # 2023-01-04 09:21:34

        cursor.executescript(create_table)
        # cursor.execute(query) - только для одной команды
        # cursor.executescript(query's) - для нескольких команд


if __name__ == '__main__':
    main()
