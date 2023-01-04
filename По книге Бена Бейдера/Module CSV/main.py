import csv
from pathlib import Path


def main():
    daily_temperatures = [
        [68, 65, 68, 70, 74, 72],
        [67, 67, 70, 72, 72, 70],
        [68, 70, 74, 76, 74, 75],
    ]

    # 1 способ
    file_path = Path.cwd() / "temperatures.csv"
    if not file_path.exists():
        file_path.touch()

    # file = file_path.open(mode="w", encoding="utf-8", newline="")
    # writer = csv.writer(file)
    #
    # for temp_list in daily_temperatures:
    #     writer.writerow(temp_list)
    #
    # file.close()

    # 2 способ (желательней)
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for temp_list in daily_temperatures:
            writer.writerow(temp_list)
        file.close()

    # Чтение csv
    with open(file_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
        file.close()

    # ['68', '65', '68', '70', '74', '72']
    # ['67', '67', '70', '72', '72', '70']
    # ['68', '70', '74', '76', '74', '75']

    # mini-task, Создать таблицу с заголовками
    people = [
        {'name': "Mikhail", 'age': 34, 'status': 'employer'},
        {'name': "Tatyana", 'age': 33, 'status': 'home worker'}
    ]
    file_path = Path.cwd() / "people_info.csv"
    if not file_path.exists():
        file_path.touch()
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "status"])
        writer.writeheader()
        writer.writerows(people)
        file.close()


if __name__ == '__main__':
    main()
