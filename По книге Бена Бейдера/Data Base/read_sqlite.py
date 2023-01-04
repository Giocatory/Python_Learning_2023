import sqlite3


def main():
    simple_query = 'SELECT * FROM People;'

    with sqlite3.connect("test_database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(simple_query)

        for row in cursor.fetchall():  # fetchall() возращает список кортежей
            print(*row)


if __name__ == '__main__':
    main()
