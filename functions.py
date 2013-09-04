#! /usr/bin/env python
#-*- coding: utf-8 -*-
import MySQLdb , time
from settings import *

try:
    conn = MySQLdb.connect(dbhost,dbuser,dbpasswd,dbname,dbport)

except MySQLdb.Error,e:
    print 'connect error %s ' % e
 
   
cur = conn.cursor()
  
  

cur.execute('SELECT * FROM em_list LIMIT 1 OFFSET 5') 
result = cur.fetchone()
print result
    

    
