def main():
    def MakeBold(fn):
        def wrapped():
            return f"<b>{fn()}</b>"

        return wrapped

    def MakeItalic(fn):
        def wrapped():
            return f"<i>{fn()}</i>"

        return wrapped

    @MakeBold
    @MakeItalic
    def hello():
        return "Hello user"

    print(hello())  # <b><i>Hello user</i></b>


if __name__ == '__main__':
    main()
