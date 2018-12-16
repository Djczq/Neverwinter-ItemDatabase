# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error


def open_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def getProfessionId(conn, profession):
    cur = conn.cursor()
    req = "SELECT profession FROM professions_translation where name='{}'".format(profession)
    cur.execute(req)
    row = cur.fetchone()
    if row == None:
        return None
    else:
        return int(row[0])

def getItemIdFromTr(conn, lang, name):
    cur = conn.cursor()
    req = "SELECT id FROM items_translation where name=\"{}\" and lang=\"{}\"".format(name, lang)
    cur.execute(req)
    row = cur.fetchone()
    if row == None:
        return None
    else:
        return int(row[0])

def getItemFromId(conn, id):
    cur = conn.cursor()
    req = "SELECT sellPrice,buyPrice,itemLevel,requiredLevel,refinementPoints FROM items where id=\"{}\"".format(id)
    cur.execute(req)
    row = cur.fetchone()
    return row


def insertItemTr(conn, itemId, lang, name):
    cur = conn.cursor()
    req = "insert into items_translation(item, lang, name) values (\"{}\", \"{}\", \"{}\")".format(itemId, lang, name)
    cur.execute(req)
    return cur.lastrowid

def insertItem(conn, sellPrice, buyPrice, itemlvl, reqlvl, rp):
    cur = conn.cursor()
    req = "insert into items(buyPrice, sellPrice, itemLevel, requiredLevel, refinementPoints) values ('{}', '{}', '{}', '{}', '{}');".format(buyPrice, sellPrice, itemlvl, reqlvl, rp)
    cur.execute(req)
    return cur.lastrowid


def insertProduction(conn, itemId, quantity, level, profession, commission, morale, time, focusMin, focusMax, proficiency):
    cur = conn.cursor()
    req = "insert into production(item, quantity, level, profession, commission, morale, time, focusMin, focusMax, proficiency) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(itemId, quantity, level, profession, commission, morale, time, focusMin, focusMax, proficiency)
    cur.execute(req)
    return cur.lastrowid


def insertCredit(conn, itemId, credit, credit1):
    cur = conn.cursor()
    req = "insert into credits(item, credit, credit1) values ('{}', '{}', '{}')".format(itemId, credit, credit1)
    cur.execute(req)
    return cur.lastrowid

def insertFullItem(conn, item):
    itemId = getItemIdFromTr(conn, item.lang, item.name)
    if item.profession != "":
            professionid = getProfessionId(conn, item.profession)
    if itemId == None:
        cur = conn.cursor()
        itemId = insertItem(conn, item.svalue, item.bvalue, item.itemlvl, item.reqlvl, item.rpvalue)
        insertItemTr(conn, itemId, item.lang, item.name)
        if item.profession != "":
            insertProduction(conn, itemId, item.quantity, item.plvl, professionid, item.commission, item.morale, item.time, item.focusMin, item.focusMax, item.proficiency)
    else:
        row = getItemFromId(conn, itemId)
        if row[0] == item.svalue and row[1] == item.bvalue and row[2] == item.itemlvl and row[3] == item.reqlvl and row[4] == item.rpvalue and item.profession != "":
            insertProduction(conn, itemId, item.quantity, item.plvl, professionid, item.commission, item.morale, item.time, item.focusMin, item.focusMax, item.proficiency)


