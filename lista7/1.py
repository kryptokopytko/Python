import re
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import requests
from bs4 import BeautifulSoup
import threading

visited_sites = []

def crawl(start_page, distance, action, visited_sites = visited_sites):
    if distance < 1 or visited_sites.count(start_page):
        return
    visited_sites += start_page
    t = threading.Thread(target = print_address, args = (start_page, ))
    t.start()
    t.join()
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
            t = threading.Thread(target = print_Python, args = (sentence.replace('\n', ' '), ))
            t.start()
            t.join()

def print_address(address):
    print("\nWeszlismy na strone: {}" .format(address))
    
def print_Python(text):
    print("{}" .format(text))



crawl('https://linux.die.net/man/2/seteuid', 2, find_python)
