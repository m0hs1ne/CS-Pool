import os
import requests
from bs4 import BeautifulSoup
import argparse

def download_images(url, save_path, extensions, depth=0, max_depth=5):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    urls = [image.get('src') for image in images]
    urls = [url for url in urls if any(url.endswith(ext) for ext in extensions)]

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for url in urls:
        download_image(url, save_path)

    if depth >= max_depth:
        return

    links = soup.find_all('a')
    links = [link.get('href') for link in links]
    links = [link for link in links if link is not None and link.startswith(url)]

    for link in links:
        download_images(link, save_path, extensions, depth=depth+1, max_depth=max_depth)

def download_image(url, save_path):
    response = requests.get(url)
    filename = os.path.join(save_path, os.path.basename(url))
    with open(filename, 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':

    DEFAULT_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    DEFAULT_MAX_DEPTH = 5
    DEFAULT_SAVE_PATH = './data/'

    parser = argparse.ArgumentParser(description='Spider program to extract all images from a website')
    parser.add_argument('url', type=str, help='URL to crawl')
    parser.add_argument('-r', action='store_true', help='recursively download images')
    parser.add_argument('-l', type=int, help='maximum depth level of recursion')
    parser.add_argument('-p', type=str, help='path to save downloaded images')
    args = parser.parse_args()

    save_path = args.p or DEFAULT_SAVE_PATH
    extensions = DEFAULT_EXTENSIONS
    max_depth = args.l or DEFAULT_MAX_DEPTH

    if args.r:
        download_images(args.url, save_path, extensions, max_depth=max_depth)
    else:
        download_images(args.url, save_path, extensions, depth=0, max_depth=0)