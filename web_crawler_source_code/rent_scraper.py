import requests
import urllib.request
import os
import pandas
import re
from bs4 import BeautifulSoup


def download_rent_data(url, download_folder):

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    print('Loading, please wait')
    # link to next page
    i = 1
    while 1:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        # items in each page
        items = soup.find_all('a', class_="result-title hdrlnk")
        headline = []
        price = []
        housing = []
        available = []
        latitude = []
        longitude = []
        urls = []
        ft = []

        for item in items:
            item_page = requests.get(item['href'])
            subsoup = BeautifulSoup(item_page.content, "html.parser")

            text = subsoup.find(id="titletextonly")
            if text:
                headline.append(text.string)
            else:
                headline.append('NA')

            text = subsoup.find(class_="price")
            if text:
                price.append(text.string)
            else:
                price.append('NA')

            text = subsoup.find(class_="housing")
            if text:
                housing.append(text.string)
            else:
                housing.append('NA')

            text = subsoup.find(attrs={'data-today_msg': "available now"})
            if text:
                available.append(text['data-date'])
            else:
                available.append('NA')

            text = subsoup.find(id="map")
            if text:
                latitude.append(text['data-latitude'])
                longitude.append(text['data-longitude'])
            else:
                latitude.append('NA')
                longitude.append('NA')

            # text = subsoup.find_all('span', class_='shared-line-bubble')
            # if text and text[1]:
            #     text = text[1].find('b')
            #     ft.append(text.string)
            # else:
            #     ft.append('NA')

            urls.append(item['href'])

        data = pandas.DataFrame({"Headline": headline, "Price": price, "Housing": housing, "Available Date": available, "Latitude": latitude, "Longitude": longitude, "URL": urls})
        file_name = '/page'+ str(i) + '.csv'
        data.to_csv(download_folder + file_name, sep=',')

        print( str(i) + ' page loaded')
        i += 1
        next_url = soup.find('a', class_="button next")['href']
        if not re.match(r'^/search/apa?', str(next_url)):
            break
        print('Still loading, please wait')
        url = 'https://pittsburgh.craigslist.org' + next_url

    print('Finished')


def main():

    download_rent_data('https://pittsburgh.craigslist.org/search/apa?query=cmu', './downloads/rent_data')



if __name__ == "__main__":
    main()