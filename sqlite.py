#!/usr/bin/python3
import sqlite3
import random
import string
import time
import os
import sys
import subprocess

default_table   ='defaultTable'
QUITE  = True if "-q" in sys.argv else False

def p(string):
    if not QUITE:
        print(string)

def db_insert(itemList, table=default_table):
    item = ",".join(repr(e) for e in itemList)
    request = """INSERT INTO %s (NAME, ADDRESS) VALUES(%s);
              """ % (table, item)
    conn.execute(request)

def db_select(id, table=default_table):
    request = """SELECT * FROM %s WHERE id=%s;
              """ % (table, id)
    cursor = conn.execute(request)
    for row in cursor:
        p(row)

def db_dropTable(table=default_table):
    request = """DROP TABLE %s
              """ % table
    p(request)
    conn.execute(request)

def db_createTable(table=default_table):
    request = '''CREATE TABLE %s
           (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
            NAME           TEXT    NOT NULL,
            ADDRESS        CHAR(100)
           );''' % table
    p(request)
    conn.execute(request)
    p("Table \"%s\" created successfully" % table);

def db_showInfo():
    #print("Database: %s" % database);
    request = """SELECT * FROM %s ORDER BY ID DESC LIMIT 5
              """ % default_table
    cursor = conn.execute(request)
    for row in cursor:
        print(row)

def db_getTableSize():
    request = """SELECT count(*) FROM %s
              """ % default_table
    cursor = conn.execute(request)
    size = [x for x in cursor][0][0] #cursor -> tuple -> value
    return size

def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def randomInsert(number):
    p("System cache cleared.")
    clearSysCache()
    p("===== Start Inserting =====")
    startTime = time.time()
    for i in range(number):
        if(i % 1000 == 0):
            p(i)
        value = randomword(100)
        #value = "mljtxalplcbstzwgwqocpdvcoqcwftyresxucgvlyscklhpzkmdiylzbirpnqswzgrvsnkgkcwvcatibeuheznnbpkbrlarchdmy"
        db_insert([value[0:5], value])
        conn.commit()
    endTime = time.time()
    elapsedTime = endTime-startTime
    p("===== End Inserting =====")
    p("Insert %s into the table" % number)
    p("Start Time    : %s" % startTime )
    p("End Time      : %s" % endTime )
    p("Time Elapsed  : %s" % str(elapsedTime))
    return elapsedTime

def select(number, size, mode="random"):
    p("System cache cleared.")
    clearSysCache()
    p("===== Start Selecting =====")
    startTime = time.time()
    lastTime = startTime
    currentTime = 0
    for i in range(number):
        if(i % 1000 == 0):
            #clearSysCache()
            currentTime = time.time()
            timeElapsed = currentTime - lastTime
            lastTime = currentTime
            p(str(i) + " " + str(timeElapsed))
        if mode=="random":
            db_select(random.randint(0,size))
        elif mode=="sequential":
            requestId = i % size
            db_select(requestId) #sequential read
        else:
            exit(-1)
    endTime = time.time()
    p("===== End Selecting =====")
    elapsedTime = endTime-startTime
    p("Select %s from the table (size = %s)" % (number,size))
    p("Start Time    : %s" % startTime )
    p("End Time      : %s" % endTime )
    p("Time Elapsed  : %s" % str(elapsedTime))
    return elapsedTime

def resetTable(number):
    print("Resetting the table: %s" % number)
    db_dropTable()
    db_createTable()
    randomInsert(number) 

def clearSysCache():
    os.system("sudo sysctl vm.drop_caches=3 > /dev/null")

############################## Start point

if len(sys.argv) is 1:
    print("""[Usage]
        ./sqlite.py --db [DB's name] --create 
        ./sqlite.py --db [DB's name] --show
        ./sqlite.py --db [DB's name] --drop
        ./sqlite.py --db [DB's name] --insert     [num of items]
        ./sqlite.py --db [DB's name] --select     [num of items]
        ./sqlite.py --db [DB's name] --select-seq [num of items]
        ./sqlite.py --db [DB's name] --reset      [num of items]
          """,  )
    sys.exit()

if "--db" in sys.argv:
    dbargv = sys.argv[sys.argv.index("--db")+1]
    database = dbargv if ".db" in dbargv else dbargv + ".db"

if not os.path.isfile(database):
    input("The database \"%s\" does not exist. Create it? (Press any key to continue)" %database)

conn = sqlite3.connect(database)
p("Opened database: %s" % database)

if "--create" in sys.argv:
    db_createTable()

db_size = db_getTableSize()

############################## After we have the table

if "--drop" in sys.argv:
    db_dropTable()

if "--show" in sys.argv:
    db_showInfo()
    print("DB Size: %s" % db_size)

if "--reset" in sys.argv:
    request= int(sys.argv[sys.argv.index("--reset")+1])
    resetTable(request)

if "--insert" in sys.argv:
    request= int(sys.argv[sys.argv.index("--insert")+1])
    randomInsert(request)

if "--select" in sys.argv:
    number = int(sys.argv[sys.argv.index("--select")+1])
    select(number, db_size)

if "--select-seq" in sys.argv:
    number = int(sys.argv[sys.argv.index("--select-seq")+1])
    select(number, db_size, "sequential")

conn.close()

