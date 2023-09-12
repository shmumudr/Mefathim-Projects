"""
Wikipedia Image and Link Scraper
=================================

This Python script allows users to scrape images from a specified Wikipedia page and save them in folders.
It also extracts random links from the page for further exploration.

Usage:
------
1. Run the script, and it will prompt you to enter a Wikipedia page's title (e.g., "food").
2. The script will then scrape images from that Wikipedia page and save them in a directory.
3. It will also follow random links from the page and continue the process up to a specified depth.


Main Execution:
---------------
The script's main execution occurs when `__name__` is equal to `"__main__"`.
It sets initial parameters and starts the scraping process.

Usage Notes:
------------
- Ensure that you have the required libraries installed before running the script.
- The script may take a significant amount of time to complete, depending on the depth and width settings.
- Be mindful of potential legal and ethical considerations when scraping websites.

Note:
-----
- You can customize the script by modifying the `width`, and `depth`
- variables to suit your scraping needs. enter this values in terminal
"""

import sys
import requests
from bs4 import BeautifulSoup
import random
import urllib.parse
import os
from random import sample
import sys

USER_INPUT = input("please enter wikipedia value: ") # Input from the user to specify the Wikipedia page title.
PATH = 'https://en.wikipedia.org/wiki/' + USER_INPUT # The URL of the Wikipedia page to start scraping.
PATH_OF_DIRECTORY = '/home/mefathim/PycharmProjects/pythonProject/wikipedia_test' # where images will be saved.
max_images_from_one_page = 5 # Maximum number of images to download from a single Wikipedia page.

# Recursively crawls Wikipedia pages, extracts and saves images, and follows random links.
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
        links = find_random_url_links(url, soup, visited_links, width)

        for link in links:
            crawl_wikipedia(link, directory, depth - 1, width, visited_links)


# downloads an image from a URL and saves it in the specified directory.
def download_image(url, name, directory):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            path = f"{directory}/{urllib.parse.quote(name)}"

            with open(path, 'wb') as file:
                file.write(response.content)
    except:
        return

# finds and returns image links from the given BeautifulSoup object
def find_image_links(soup):
    all_links = soup.find_all('img', class_='mw-file-element')

    correct_links = [i.get('src') for i in all_links]
    correct_links = random.sample(correct_links, min(len(correct_links), max_images_from_one_page))
    for link in range(len(correct_links)):
        if correct_links[link].startswith('//'):
            correct_links[link] = 'https:' + correct_links[link]
        elif correct_links[link].startswith('/'):
            correct_links[link] = 'https:/' + correct_links[link]
    return correct_links

# extracts and returns the title of a Wikipedia page from the BeautifulSoup object.
def get_title(soup):
    title = soup.title
    title_str = title.string
    title_name = title_str.split()[0]
    return title_name

# Generates a valid file name for an image based on its URL.
def image_name_from_url(url):
    name = url.rsplit("/", 1)[-1]
    if len(name) <= 20:
        return name
    else:
        return name[-20:]

# Finds random Wikipedia page links from the given BeautifulSoup object.
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

# Fetches a web page, parses its HTML, and returns a BeautifulSoup object.
def create_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
    return soup


def main():
    if len(sys.argv) == 3:
        width = int(sys.argv[1])
        depth = int(sys.argv[2])

    visited_links = set()
    crawl_wikipedia(PATH, PATH_OF_DIRECTORY, depth, width, visited_links)


if __name__ == "__main__":
    main()
