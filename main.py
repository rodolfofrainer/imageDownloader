from bs4 import BeautifulSoup
import requests

links = []

with open('combisteel_images.txt', 'r') as file:
    links.append(file.readlines())

for link in links[0]:
    scrapeLink = link
    page = requests.get(scrapeLink)
    # soup = BeautifulSoup(page.content, 'html.parser')
    print(page)
