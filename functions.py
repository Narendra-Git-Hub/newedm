#! /usr/bin/env python
#-*- coding: utf-8 -*-
import MySQLdb , time
from settings import *

try:
    conn = MySQLdb.connect(dbhost,dbuser,dbpasswd,dbname,dbport)

except MySQLdb.Error,e:
    print 'connect error %s ' % e
   
cur = conn.cursor()
  
  
#get the email info
def get_email_info():
    
    ctime = int(time.time())
    
    sql = 'SELECT sendtime, colid, amount, status FROM send_list'
    condition = ' WHERE sendtime <= %d AND status = %d' % (ctime,1)
    sql = sql + condition
    
    cur.execute(sql)
    result = cur.fetchone()
    return result


#combination the email list
def create_mail_list():

    mailinfo = get_email_info()
    send_amount = mailinfo[2]
    send_colid = mailinfo[1]
   
    for i in range(send_amount):
         sql = 'SELECT email FROM email_list WHERE colid = %d LIMIT 1 OFFSET %d' % (send_colid,i)
         cur.execute(sql)
         result = cur.fetchone()
         print result 

create_mail_list()

