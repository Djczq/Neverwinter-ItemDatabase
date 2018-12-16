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
        for it in items:
            if len(it.materials) > 1:
                for m in it.materials:
                    r = dr.insertMaterial(conn, it.lang, it.name, m[0], m[1])
                    if r == None:
                        print "Item not found"
                    if r == -1:
                        print "Material not found : ", m[1]
    