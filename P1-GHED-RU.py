#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
def correct_url():
    print("Что ищем?")
    print('1. Взрывчатка')
    print('2. Чай')
    #itemsearch = '1'
    itemsearch = input('=> ')
    if itemsearch == '1':
        add_url = '1'
        pass
    elif itemsearch == '2':
        add_url = '21'
        pass
    else:
        pass
    return add_url
def find():
    print('-----------------------------------------------')
    print('Elite Dangerous: Commodity finder (Alpha build)') #parcer (not API)
    print('-----------------------------------------------')
    add_url = correct_url() #добавляем нужный индекс
    print('-----------------------------------------------')
    url = 'https://eddb.io/commodity/' + add_url #итоговый индекс получается таким образом
    response = requests.get(url)  #запрашиваем страницу #print(response.text) просмотреть код страницы
    create_file('rqst.html', response.text) #записываем полученный текст в отдельный файл
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find('div', {'class': 'table-wrap'})
    k=1
    set1 = []# станция
    set2 = []# система
    set3 = []# сейчас это словарь, но потом можно переделать под генератор для заголовка
    itemcount = 6 # если выставить больше 6, то вся табличка из консоли съедет, но как переделать таблицу в вертикальную пока без понятия
    itemcount2 = itemcount*2 + 1
    for gg in results.find_all('a', 'href' == True):
        if k < itemcount2:
            if k%2 != 0:
                set1.append(gg.text)
            elif k%2 == 0:
                set2.append(gg.text)
            else:
                pass
        else:
            break
        pass
        k=k+1
    prices = []
    procents = []
    quantity = []
    padsize = []
    howlong = []
    itemcount3 = itemcount*6 + 1
    for qq in results.find_all('span'):
        u = k % 6
        if k < itemcount3:
            if u == 1:
                prices.append(qq.text)
            elif u == 2:
                pass
            elif u == 3:
                quantity.append(qq.text)
            elif u == 4:
                padsize.append(qq.text)
            elif u == 5:
                pass
            elif u == 0:
                howlong.append(qq.text)
            else:
                pass
        else:
            break
        k=k+1
    set3=[]
    headervalue = itemcount
    ww = 1
    while ww != headervalue + 1:
        set3.append(str(ww))
        ww = ww + 1
    table_data = [set3, set1, set2, padsize, howlong, quantity, prices]
    print_pretty_table(table_data)
    print('-----------------------------------------------')
def print_pretty_table(data, cell_sep=' | ', header_separator=True):
    rows = len(data)
    cols = len(data[0])

    col_width = []
    for col in range(cols):
        columns = [data[row][col] for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    separator = "-+-".join('-' * n for n in col_width)

    for i, row in enumerate(range(rows)):
        if i == 1 and header_separator:
            print(separator)

        result = []
        for col in range(cols):
            item = data[row][col].rjust(col_width[col])
            result.append(item)

        print(cell_sep.join(result))
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)
find()
