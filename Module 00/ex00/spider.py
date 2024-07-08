import argparse
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_image(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(path, url.split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")

def spider(url, max_depth, current_depth=0, path='./data/', visited=None):
    if visited is None:
        visited = set()
    
    if current_depth > max_depth or url in visited:
        return
    
    visited.add(url)
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for img in soup.find_all('img'):
            img_url = urljoin(url, img.get('src'))
            if any(img_url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']):
                download_image(img_url, path)
        
        if current_depth < max_depth:
            print(f"Depth: {current_depth} - Visiting: {url}")
            for link in soup.find_all('a'):
                next_url = urljoin(url, link.get('href'))
                if urlparse(next_url).netloc == urlparse(url).netloc:
                    spider(next_url, max_depth, current_depth + 1, path, visited)
    
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Spider program to extract images from websites")
    parser.add_argument("url", help="The URL to start crawling from")
    parser.add_argument("-r", action="store_true", help="Recursively download images")
    parser.add_argument("-l", type=int, default=5, help="Maximum depth level for recursive download")
    parser.add_argument("-p", default="./data/", help="Path to save downloaded files")
    
    args = parser.parse_args()
    
    os.makedirs(args.p, exist_ok=True)
    
    if args.r:
        spider(args.url, args.l, path=args.p)
    else:
        spider(args.url, 0, path=args.p)

if __name__ == "__main__":
    main()