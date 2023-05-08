import requests
import threading

HEADERS = {
    'User-Agent': 'Mozilla/5.0 \
        (Macintosh; Intel Mac OS X 10_10_1) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/39.0.2171.95 Safari/537.36'}


def download_image(url, index):
    page = requests.get(url.strip(), headers=HEADERS)
    with open(f'images/{index}.jpg', 'wb') as file:
        file.write(page.content)
    print(f'Downloaded {url}')


with open('combisteel_images.txt', 'r') as file:
    links = file.readlines()

threads = []
for index, link in enumerate(links[:5]):
    thread = threading.Thread(target=download_image, args=(link, index))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
