# -*- coding: utf-8 -*-
import requests
import docx
import re
import time
import os
from bs4 import BeautifulSoup

if __name__ == "__main__":

    __start_time__ = time.time()

    # Начальные значения для номеров файлов

    s_count = 175
    m_count = 175
    l_count = 175

    # Получение исходных статей

    for i in range(1, 5):
        req_main = requests.get("https://www.chitalnya.ru/other/87/p" + str(i) + "/3/")
        src_main = req_main.text

        soup_main = BeautifulSoup(src_main, "lxml")

        with open("index.html", "w", encoding="utf-8") as file:
            file.write(src_main)

        # Сбор ссылок
        
        articles_lib = soup_main.select('.col-md-12.x1cls .col-md-6.x2')
        urls_lib = []
        for article in articles_lib:
            urls_lib.append("https://www.chitalnya.ru" + article.find(class_='lnkgrey').get("href"))

        # Проверка количества отработанных ссылок

        print(len(urls_lib), "ссылок")
        __test_count__ = 0

        # Счётчик получившихся текстов

        __l_articles_count__ = 0

        # Создание рабочих каталогов

        if not os.path.exists("L"):
            print("Была создана директория L")
            os.makedirs("L/")

        # Работа со статьями

        for url in urls_lib:
            req = requests.get(url)

            soup = BeautifulSoup(req.text, "lxml")

            # Переменные для подсчёта количества и записи в файл

            words_count = 0
            chars_count = 0
            all_chars_count = 0
            article_text = ""

            # Счётчик отработанных ссылок

            __test_count__ += 1

            # Сбор текста

            for tab in soup.select('.col-md-9.x2 > b > span'):
                article_text += str(tab.text)
                tab_text = str(tab.text)
                tab_text.replace('-', '')
                words_count += len(re.findall(r'\w+', tab_text))
                all_chars_count += len(tab_text)
                chars_count += len(re.findall(r'\S', tab_text))

            # Запись текста в необходимый .docx и запись метаданных .txt

            if (words_count > 901) and (words_count < 2000):
                __l_articles_count__ += 1
                if l_count > 209:
                    continue
                with open("L/" + str(l_count) + ".txt", "w", encoding="utf-8") as file:
                    file.write(f"{url}\n07.04.2022\n{words_count}\n{all_chars_count}, {chars_count}\n7\n")
                # new_doc = docx.Document()
                # new_doc.add_paragraph(article_text)
                # new_doc.save("E:/PycharmProjects/L/" + str(l_count) + ".docx")
                l_count += 1

        # Итог работы программы: количество отработанных ссылок и время работы

        print(f"{__test_count__} ссылок обработано\n"
              f"S: 0/34\nM: 0/34\nL: {__l_articles_count__}/34\n"
              f"Время работы: {time.time() - __start_time__}")
