# import requests
# from bs4 import BeautifulSoup
# import random

# # https://nukadeti.ru/skazki

# def fetch_html(url):
#     response = requests.get(url)
#     return response.text

# def parce_story_links(html):
#     soup = BeautifulSoup(html, "lxml")
#     urllist = []
#     for link in soup.find_all("a", class_="title"):
#         urllist.append(f"https://nukadeti.ru/{link.get("href")}")
#     return urllist

# def fetch_random_story()



# def main():
#     url = "https://nukadeti.ru"
#     html = fetch_html(url)
#     urllist = parce_story_links(html)
#     print (urllist)


# main()
