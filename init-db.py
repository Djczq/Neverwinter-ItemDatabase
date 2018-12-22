# -*- coding: utf-8 -*-

import sqlite3, os
import sqlite.databaseRequest as dr
import parser.itemsParser as iP

if __name__ == "__main__":
    if os.path.exists("local.db"):
        os.remove("local.db")
    with dr.open_db("local.db") as conn:
        with open("sqlscripts/create-tables.sql", mode="r") as f:
            sql = f.read()
            conn.executescript(sql)
        with open("sqlscripts/languages.sql", mode="r") as f:
            sql = f.read()
            conn.executescript(sql)
        with open("sqlscripts/professions.sql", mode="r") as f:
            sql = f.read()
            conn.executescript(sql)
        items = iP.getProfessionItems()
        for it in items:
            print it
            dr.insertFullItem(conn, it)
        insertFailed = []
        for it in items:
            if len(it.materials) > 1:
                for m in it.materials:
                    r = dr.insertMaterial(conn, it.lang, it.name, m[0], m[1])
                    if r == None:
                        print "Item not found"
                    if r == -1:
                        t = (it.name,) + m
                        insertFailed.append(t)
                        print "Material not found : ", m[1]

        print "insert missing"
        for m in insertFailed:
            infos = iP.processItemPage("https://neverwinter.gamepedia.com/" + m[2].replace(' ', '_'))
            itemId = dr.getItemIdFromTr(conn, "eng", m[2])
            if itemId == None:
                itemId = dr.insertItem(conn, infos[0], infos[1], infos[2], infos[3], infos[4])
                dr.insertItemTr(conn, itemId, "eng", m[2])
            r = dr.insertMaterial(conn, "eng", m[0], m[1], m[2])
            if r == None:
                print "Item not found"
            if r == -1:
                print "Material not found : ", m[1]
