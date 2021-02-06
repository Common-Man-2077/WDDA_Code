import requests
from bs4 import BeautifulSoup
import pandas as pd
import random


data = []
article_id = 0
# Selecting the year to extract information
selected_years = list(range(2016, 2021))
# Selecting the day to extract information
selected_days = list(range(1, 366))
n = len(selected_days)

urls = 'https://towardsdatascience.com/archive/{0}/{1:02d}/{2:02d}'


def convert_day(day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m = 0
    d = 0
    while day > 0:
        d = day
        day -= month_days[m]
        m += 1
    return (m, d)


def get_claps(claps_str):
    if (claps_str is None) or (claps_str == '') or (claps_str.split is None):
        return 0
    split = claps_str.split('K')
    claps = float(split[0])
    claps = int(claps*1000) if len(split) == 2 else int(claps)
    return claps


for year in selected_years:
    i = 1
    for d in selected_days:
        month, day = convert_day(d)
        date = '{0}-{1:02d}-{2:02d}'.format(year, month, day)
        print(f'{i} / {n} ; {date}')
        i = i + 1
        response = requests.get(urls.format(
            year, month, day), allow_redirects=True)
        if not response.url.startswith(urls.format(year, month, day)):
            continue
        page = response.content
        soup = BeautifulSoup(page, 'html.parser')
        articles = soup.find_all(
            "div", class_="streamItem streamItem--postPreview js-streamItem")
        for article in articles:
            article_id += 1
            title = article.find(
                "h3", class_="graf--h3")
            if title is None:
                continue
            title = title.contents[0]

            article_url = article.find_all("a")[3]['href'].split('?')[0]

            claps = get_claps(article.find_all("button")[1].contents[0])

            reading_time = article.find("span", class_="readingTime")
            reading_time = 0 if reading_time is None else int(
                reading_time['title'].split(' ')[0])

            responses = article.find_all("a")
            if len(responses) == 7:
                responses = responses[6].contents[0].split(' ')
                if len(responses) == 0:
                    responses = 0
                else:
                    responses = responses[0]
            else:
                responses = 0

            data.append([article_id, article_url, title,
                         claps, responses, reading_time, date])


medium_df = pd.DataFrame(data, columns=[
    'id', 'url', 'title', 'claps', 'responses',
    'reading_time', 'date'])
medium_df.to_csv('medium_data.csv', encoding='utf-8-sig', index=False)
