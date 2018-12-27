# -*- coding: utf-8 -*-
import sqlite3
import databaseRequest as dr

def listAll(conn):
    list = []
    ids = dr.getAllId(conn)
    for i in ids:
        id = i[0]
        name = dr.getItemTrFromId(conn, id, "eng")[0]
        item = dr.getItemInfoFromId(conn, id)
        profession = dr.getProfessionInfoFromId(conn, id)
        r = name + ","
        r += str(item[0]) + ","
        r += str(item[1]) + ","
        r += str(item[2]) + ","
        r += str(item[3]) + ","
        r += str(item[4])
        if len(profession) == 0:
            r += ",,,,,,"
            list.append(r)
        else:
            for p in profession:
                r2 = r + ","
                pname = dr.getProfessionTrFromId(conn, p[2], "eng")[0]
                r2 += str(p[0]) + ","
                r2 += str(p[1]) + ","
                r2 += pname + ","
                r2 += str(p[3]) + ","
                r2 += str(p[4]) + ","
                r2 += str(p[5])
                list.append(r2)
    return list

def printAll(conn):
    list = listAll(conn)
    for i in list:
        print i

def printAllOrdered(conn):
    list = listAll(conn)
    for i in sorted(list):
        print i

