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
        
    