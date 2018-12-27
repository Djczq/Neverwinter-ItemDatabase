# -*- coding: utf-8 -*-

import sys
import sqlite.databaseRequest as dr
import sqlite.databasePrint as dp

if __name__ == "__main__":
    print sys.argv[1]
    if len(sys.argv) > 1:
        with dr.open_db("local.db") as conn:
            if sys.argv[1] == "ordered":
                dp.printAllOrdered(conn)
            if sys.argv[1] == "list":
                dp.printAll(conn)