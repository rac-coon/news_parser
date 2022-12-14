import requests
import time
import json
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # print("Введите нужную дату 2022/01/01")
    # in_date = input()
    #
    # url = "https://echo.msk.ru/news/" + in_date + ".html"
    #
    # headers = {
    #     "Accept": "*/*",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
    # }
    #
    # req = requests.get(url, headers=headers)
    # src = req.text
    #
    # with open("index.html", "w", encoding="utf-8") as file:
    #     file.write(src)
    #
    with open("text.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    text = soup.select('.article-view')
    print(text)
    #
    # all_news = {}
    # count = 0
    # e_count = 0
    # time_req = time.strftime("%d_%m_%y-%H_%M")

    # with open(time_req + ".txt", "w", encoding="utf-8") as file:
    #     for el in soup.select('div .preview.newsblock.iblock'):
    #         if el.find_all(class_='datetime') and el.select('h3 > [href]'):
    #             data_url = el.find(class_='share').get("data-url")
    #             date = el.select('.datetime')[0].text
    #             title = el.select('h3 > [href]')[0].text
    #             if not el.select('.meta > .comm > .count'):
    #                 comments = "ЗАКРЫТЫ"
    #             else:
    #                 comments = el.select('.meta > .comm > .count')[0].text
    #             if not el.select('.meta > .view > .count'):
    #                 views = "СКРЫТЫ"
    #             else:
    #                 views = el.select('.view > .count')[0].text
    #             print(data_url, date, title, " | ", comments, "комментариев", views, "просмотров")
    #             count += 1
    #             file.write(f" {data_url} {date} {title} \n {views} просмотров {comments} комментариев \n")
    #         else:
    #             e_count += 1
    #             pass
    #
    # print(f"\n[{e_count}] Объектов из обсуждаемого не было ошибочно взято\n[{count}] новостей")
