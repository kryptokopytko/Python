import matplotlib.pyplot as plt
import math
from bs4 import BeautifulSoup
import requests
import pandas as pd

def plinflation():
    res = requests.get(f'https://stat.gov.pl/obszary-tematyczne/ceny-handel/wskazniki-cen/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-pot-inflacja-/miesieczne-wskazniki-cen-towarow-i-uslug-konsumpcyjnych-od-1982-roku/')
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find('table', class_ = "tabelkaszara")

    data = []
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    data2022 = data[3]
    data2021 = data[4]
    data2020 = data[5]
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plt.plot(months, data2020)
    plt.ylabel('inflacja w Polsce, Grudzień poprzedniego roku = 100')
    plt.plot(months, data2021)
    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], data2022)
    plt.legend(['2020', '2021', '2022'])    
    plt.show()

def usinflation():
    res = requests.get(f'https://www.usinflationcalculator.com/inflation/historical-inflation-rates/')
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find('table')

    data = []
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    length = len(data)
    data2022 = data[length - 1]
    data2021 = data[length - 2]
    data2020 = data[length - 3]
    del data2022[10]
    del data2020[12]
    del data2021[12]
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plt.plot(months, data2020)
    plt.ylabel('inflacja w US')
    plt.plot(months, data2021)
    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], data2022)
    plt.legend(['2020', '2021', '2022'])    
    plt.show()

def predictions():
    res = requests.get(f'https://stat.gov.pl/obszary-tematyczne/ceny-handel/wskazniki-cen/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-pot-inflacja-/miesieczne-wskazniki-cen-towarow-i-uslug-konsumpcyjnych-od-1982-roku/')
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find('table', class_ = "tabelkaszara")
    data = []
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    datap = []
    for i in range (0, 12):
        datap.append([(float(data[4][i].replace(",", ".")) + float(data[5][i].replace(",", "."))) / 2])
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plt.plot(months, datap)
    plt.ylabel('przewidywania')
    plt.show()

usinflation()
plinflation()
predictions()