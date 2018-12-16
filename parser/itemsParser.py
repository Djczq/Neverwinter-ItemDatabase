# -*- coding: utf-8 -*-
#pip install requests BeautifulSoup4

import requests
from bs4 import BeautifulSoup
from classes import Item


def htmlToCopper(contents):
    value = 0
    try:
        l = len(contents)
        if l > 1:
            for k in range(1, l, 2):
                value += int(contents[k]) * 100 ** ((l - k)/2)
        return value
    except:
        return -1

def processRow(website, row, profession, lang):
    columns = row.find_all('td')
    if len(columns) == 0:
        return None
    try:
        plvl = columns[0].string.strip()
    except:
        plvl = -1

    try:
        name = columns[2].a.string.strip()
    except:
        name = -1

    try:
        commission = htmlToCopper(columns[3].contents)
    except:
        commission = -1

    try:
        profeciency = columns[4].string.strip()
    except:
        profeciency = -1

    try:
        focus = columns[5].string.strip()
    except:
        focus = -1
        #    print "materials", columns[6].prettify()
    try:
        quantity = columns[7].div.contents[0].string.replace('x','').strip()
    except:
        quantity = -1

    try:
        morale = columns[8].string.strip()
    except:
        morale = -1

    try:
        time = columns[9].string.strip()
    except:
        time = -1

    bvalue = 0
    svalue = 0
    rpvalue = 0
    itemlvl = 0
    reqlvl = 0
    try:
        item_ref = columns[7].a['href']
        item_page = requests.get(website + item_ref).text
        item_html = BeautifulSoup(item_page,"html.parser")
        trs = item_html.find('div', 'infobox').find_all('tr')
        for tr in trs:
            if tr.th.string == None:
                continue
            if tr.th.string.strip() == "Buy value:":
                bvalue = htmlToCopper(tr.td.contents)
            if tr.th.string.strip() == "Sale value:":
                svalue = htmlToCopper(tr.td.contents)
            if tr.th.string.strip() == "Refinement point:":
                try:
                    rpvalue = int(tr.td.contents[1].string.strip())
                except ValueError:
                    rpvalue = 0
            if tr.th.string.strip() == "Item level:":
                try:
                    itemlvl = int(tr.td.string.strip())
                except ValueError:
                    itemlvl = 0
            if tr.th.string.strip() == "Requires level:":
                try:
                    reqlvl = int(tr.td.string.strip())
                except ValueError:
                    reqlvl = 0
    except:
        bvalue = -1
        svalue = -1
        rpvalue = -1
        itemlvl = -1
        reqlvl = -1
    if focus != -1:
        try:
            focusMin = int(focus.split('-')[0].strip())
        except ValueError:
            focusMin = 0
        try:
            focusMax = int(focus.split('-')[1].strip())
        except ValueError:
            focusMax = 0
    else:
        focusMin = -1
        focusMax = -1

    return Item.Item(name, lang, svalue, bvalue, itemlvl, reqlvl, rpvalue, quantity, plvl, profession, commission, morale, time, focusMin, focusMax, profeciency)

def getItemsFromTable(website, table, profession, lang):
    list = []
    for row in table:
        item = processRow(website, row, profession, lang)
        if item != None:
            list.append(item)
    return list


def getItemsFromProfessionOnGamepedia(profession):
    website="https://neverwinter.gamepedia.com/"
    page = requests.get(website + profession).text
    html = BeautifulSoup(page,"html.parser")
    table = html.find('table', "wikitable").tbody.find_all('tr')
    return getItemsFromTable(website, table, profession, "eng")

def getProfessionItems():
    professions = [ "Blacksmithing", "Armorsmithing", "Alchemy", "Gathering", "Artificing", "Jewelcrafting", "Leatherworking", "Tailoring" ]
    listItem = []

    for p in professions:
        listItem += getItemsFromProfessionOnGamepedia(p)
    return listItem

