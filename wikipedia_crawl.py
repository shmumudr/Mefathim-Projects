import sys
import requests
from bs4 import BeautifulSoup
import random
import urllib.parse
import os
from random import sample

# USER_INPUT = input("please enter wikipedia value: ")
PATH = 'https://en.wikipedia.org/wiki/food'
PATH_OF_DIRECTORY = '/home/mefathim/PycharmProjects/pythonProject'
max_images_from_one_page = 21


def crawl_wikipedia(url, directory, depth, width, visited_links):
    soup = (create_soup(url))
    image_links = find_image_links(soup)
    page_title = get_title(soup)
    # current_directory = f"{directory}/{page_title}"
    current_directory = f"{directory}/{urllib.parse.quote(page_title)}"

    os.makedirs(current_directory, exist_ok=True)

    for link in image_links:
        image_name = image_name_from_url(link)
        download_image(link, image_name, current_directory)
    if depth > 0:
        # links = find_random_url_links(soup, visited_links, width)
        links = find_random_url_links(url, soup, visited_links, width)

        for link in links:
            crawl_wikipedia(link, directory, depth - 1, width, visited_links)


# recive image's url and download the image
def download_image(url, name, directory):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            # path = f"{directory}/{name}"
            path = f"{directory}/{urllib.parse.quote(name)}"

            with open(path, 'wb') as file:
                file.write(response.content)
    except:
        return



def find_image_links(soup):
    all_links = soup.find_all('img', class_='mw-file-element')

    correct_links = [i.get('src') for i in all_links]
    for link in range(len(correct_links)):
        if correct_links[link].startswith('//'):
            correct_links[link] = 'https:' + correct_links[link]
        elif correct_links[link].startswith('/'):
            correct_links[link] = 'https:/' + correct_links[link]
    return correct_links


def get_title(soup):
    title = soup.title
    title_str = title.string
    title_name = title_str.split()[0]
    return title_name


def image_name_from_url(url):
    name = url.rsplit("/", 1)[-1]
    if len(name) <= 20:
        return name
    else:
        return name[-20:]


def find_random_url_links(url, soup, visited_links, width):
    all_links = set()
    for link in soup.find_all('a', href=True):
        reference = (link.get('href'))
        wiki_prefix = reference.startswith('/wiki')
        not_special_page = ':' not in reference
        not_yet_visited = reference not in visited_links
        reference = urllib.parse.urljoin(url, reference)
        if wiki_prefix and not_special_page and not_yet_visited:
            all_links.add(reference)
    randomly_links = random.sample(list(all_links), min(len(list(all_links)), width))

    return randomly_links


def create_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
    return soup


def main():
    width = 5
    depth = 3
    visited_links = set()
    crawl_wikipedia(PATH, PATH_OF_DIRECTORY, depth, width, visited_links)


if __name__ == "__main__":
    main()


