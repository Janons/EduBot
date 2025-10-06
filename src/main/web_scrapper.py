from bs4 import BeautifulSoup
import requests


# scrapper for the news
def news_scrapper():
    source = requests.get("https://www.edisu.piemonte.it/").text
    soup = BeautifulSoup(source, "lxml")
    news_list = []

    # news_part = soup.find(class_="col-md-4 no-padding")

    news_container = soup.find("div", {id: "quicktabs-tabpage-notizie_categorie-0"})

    if news_container:
        # Get all news items (views-row)
        news_items = news_container.find_all("div", class_="views-row")
        # print(news_items)

        for items in news_items:

            news_href = items.find_("a", href=True)
            date_time_span = items.find("span")

            if news_href and len(news_list) < 5:
                news_list.append((date_time_span.text, news_href["href"]))

    print(news_list)


if __name__ == "__main__":

    news_scrapper()
