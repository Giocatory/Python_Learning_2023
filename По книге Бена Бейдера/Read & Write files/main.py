import pathlib


def main():
    file_path_txt = "lorem_text.txt"
    file_path_csv = "exp.csv"

    with open(file_path_txt, mode="r", encoding="utf-8") as file:
        for line in file.readlines():
            print(line, end=' ')

        # text = file.read()
        # print(text)  # Выводит весь текст файла

        file.close()

    print("\n\n")

    with open(file_path_csv, mode="r", encoding="1251") as file:  # Кодировка Windows
        for line in file.readlines():
            print(line, end=' ')
        file.close()

    # Создать фаил, если его нет
    if not (pathlib.Path.cwd() / "exp.txt").exists():
        (pathlib.Path.cwd() / "exp.txt").touch()

    # Запись файла (a - дописать в конец файла, w - перезаписать)
    with open("exp.txt", mode="w", encoding="utf-8") as file:
        names = ["Mikhail", "Tatyana", "Margarita", "Varvara"]
        for i in range(len(names)):
            file.write(f"{i+1}) Hello {names[i]}!\n")
        file.close()


if __name__ == "__main__":
    main()
