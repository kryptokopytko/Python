import re
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import requests
from bs4 import BeautifulSoup

visited_sites = []

def crawl(start_page, distance, action, visited_sites = visited_sites):
    if distance < 1 or visited_sites.count(start_page):
        return
    visited_sites += start_page
    print("\nWeszlismy na strone: ", start_page)
    http = httplib2.Http()
    status, response = http.request(start_page)

    r = requests.get(start_page)
    action(BeautifulSoup(r.content, 'html.parser'))

    for link in BeautifulSoup(response, parse_only = SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href'):
            if re.match("https://", link['href']) or re.match("http://", link['href']):
                crawl(link['href'], distance - 1, action)
    

def find_python(soup):
    sentences = soup.text.split('.')
    for sentence in sentences:
        if "Python" in sentence:
            print(sentence.replace('\n', ' '))


crawl('http://www.ii.uni.wroc.pl', 3, find_python)
