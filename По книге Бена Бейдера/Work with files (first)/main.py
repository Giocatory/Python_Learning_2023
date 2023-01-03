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

    # Создание файла
    if not (pathlib.Path.cwd() / "data" / "Hello.txt").exists():
        new_file = pathlib.Path.cwd() / "data" / "Hello.txt"
        new_file.touch()


if __name__ == "__main__":
    main()
