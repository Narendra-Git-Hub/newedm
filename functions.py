#! /usr/bin/env python
#-*- coding: utf-8 -*-
import MySQLdb
from settings import *

try:
    conn = MySQLdb.connect(dbhost,dbuser,dbpasswd,dbname,dbport,charset='utf8')
    cur = conn.cursor()
    cur.execute('SELECT * from em_data limit 3')

    result = cur.fetchall()
    for rows in result:
        print rows

except MySQLdb.Error,e:
    
    print 'connect error %s ' % e
