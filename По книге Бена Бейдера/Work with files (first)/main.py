import pathlib


def main():
    print(pathlib.Path.home())  # корневая папка -> C:\....
    print(pathlib.Path.cwd())  # путь до файла -> D:\.....

    path = pathlib.Path.cwd() / "files" / "exp.txt"  # Задаем путь к файлу
    print(path.exists())  # True -> да, такой фаил имеется
    print(path.is_file())  # True -> Путь ведет к файлу?
    print(path.is_dir())  # False -> Путь ведет к каталогу?

    # создание папки (директории)
    if not (pathlib.Path.cwd() / "data").exists():
        new_dir = pathlib.Path.cwd() / "data"
        new_dir.mkdir()
    # Или можно проще, без условия: new_dir.mkdir(exist_ok=True)

    # Создание файла
    new_file = pathlib.Path.cwd() / "data" / "Hello.txt"
    new_file.touch(exist_ok=True)

    # Просмотр содержимого директории (сокращаю полный путь, до названия файла)
    for path in pathlib.Path.cwd().iterdir():
        view = str(path)
        view_mass = view.split("\\")
        print(view_mass[-1])
    # data
    # files
    # main.py

    # поиск файлов в директории и подкаталогах (сокращаю полный путь, до названия файла)
    for file in pathlib.Path.cwd().glob("**/*.txt"):
        view = str(file)
        view_mass = view.split("\\")
        print(view_mass[-1])
    # Hello.txt
    # exp.txt


if __name__ == "__main__":
    main()
