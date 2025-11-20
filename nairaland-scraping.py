from bs4 import BeautifulSoup
import requests
import csv 
from urllib.request import urlopen, Request
import time
from fake_useragent import UserAgent

ua = UserAgent()

categories = [
    "politics", "business", "education",  "sports", "tv-movies", "music-radio"
]

page_numbers = range(0,21)

base_url ="https://www.nairaland.com/{category}{page_number}"

def get_soup(base_url, category, page_number):
    if page_number == 0:
        url = base_url.format(category=category, page_number="")
    else:
        url = base_url.format(category=category, page_number=f"/{page_number}")
    print(url)
    try:
        time.sleep(3)
        header = {'User-Agent': ua.random}
        request = Request(url, headers=header)
        response = urlopen(request)
        html_text = response.read()
        
        if response.getcode() == 200:
            soup = BeautifulSoup(html_text, "lxml")
            print(f"Successfully accessed the {url}")
            return soup 
        else: 
            print(f"Failed to access the {url} with status code {response.getcode()}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def get_data(soup, category):
    page_data = []
    table_tags = soup.find_all("table")
    post_table = table_tags[2]
    for post in post_table.find_all("tr")[1:]:
        headline = post.find("b").get_text(strip=True)
        link = post.find_all("a")[1]["href"]
        category = category
        row = {
            "headline": headline,
            "link": link,
            "category": category
        }
        print(row)
        page_data.append(row)
    return page_data


with open("data/raw/raw-nairaland-headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["headline", "link", "category"])
    writer.writeheader()

    for category in categories:
        for page_number in page_numbers:
            soup = get_soup(base_url, category, page_number)
            if soup:
                page_data = get_data(soup, category)
                writer.writerows(page_data)
