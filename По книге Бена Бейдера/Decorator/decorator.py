# Декоратор - это функция, ожидающая ДРУГУЮ функцию в качестве параметра
def main():
    def MakeBold(func):
        def wrapped():
            return f"<b>{func()}</b>"

        return wrapped

    def MakeItalic(func):
        def wrapped():
            return f"<i>{func()}</i>"

        return wrapped

    @MakeBold
    @MakeItalic
    def hello():
        return "Hello user"

    print(hello())  # <b><i>Hello user</i></b>


if __name__ == '__main__':
    main()
