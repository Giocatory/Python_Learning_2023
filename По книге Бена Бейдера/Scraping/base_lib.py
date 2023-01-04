from urllib.request import urlopen


def main():
    url = "https://habr.com/ru/all/"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)  # выводит полность весь HTML страницы
    print()

    start_index = html.find("<title>") + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    print(title)  # Все публикации подряд / Хабр


if __name__ == '__main__':
    main()
