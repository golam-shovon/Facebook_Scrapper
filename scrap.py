from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import mysql.connector
from time import sleep
con = mysql.connector.connect(host="localhost",user="root",passwd="",database="facebook",use_unicode=True,charset="utf8")
cursor = con.cursor ()
sql = "INSERT INTO fbarticle(article,artilink,artiname,tag) VALUES ( %s,%s,%s,%s)"

browser = webdriver.Firefox()
browser.get('https://mobile.facebook.com/groups/22012931789?bac=MTUzNTkwMTI3MzoxMDE1NTI3NTMwOTMzMTc5MDoxMDE1NTI3NTMwOTMzMTc5MCwwOjc6&multi_permalinks&refid=18')
sleep(30)
print('wait done')

for i in range(1, 10000):
    print(' done')
    for elem in browser.find_elements_by_link_text('More'):
        s=elem.get_attribute("href")
        soup=BeautifulSoup(requests.get(elem.get_attribute("href")).content,'html.parser')
    try:
        browser.implicitly_wait(30)
        p=soup.find('div', {'class': '_5rgt _5nk5'}).get_text()
        val=(p,s,"","")
        cursor.execute (sql,val)
        con.commit ()
        print('commited')
        pass
    except AttributeError:
        pass    
    try:
        browser.implicitly_wait(30)
        p=soup.find('div', {'class': 'bo'}).get_text()
        val=(p,"","","")
        cursor.execute (sql,val)
        con.commit ()
        print('commited')
        pass
    except AttributeError:
        print('nada')
        pass
    try:
        browser.implicitly_wait(10)
        p=soup.find('div', {'class': 'bp'}).get_text()
        val=(p,s,"","")
        cursor.execute (sql,val)
        con.commit ()
        print('commited')
        pass
    except AttributeError:
        print('nada')        
        pass
    try:
        browser.implicitly_wait(10)
        p=soup.find('div', {'class': 'ba'}).get_text()
        val=(p,"","","")
        cursor.execute (sql,val)
        con.commit ()
        print('commited')
        pass
    except AttributeError:
        print('nada')       
        pass
    try:
        browser.implicitly_wait(10)
        p=soup.find('div', {'class': 'bn'}).get_text()
        val=(p,s,"","")
        cursor.execute (sql,val)
        con.commit ()
        print('commited')
        pass
    except AttributeError:
        print('nada') 
        pass
    try:
        browser.implicitly_wait(10)
        p=soup.find('div', {'class': 'bq'}).get_text()
        val=(p,s,"","")
        cursor.execute (sql,val)
        con.commit ()
        print('commited')
        pass
    except AttributeError:
        print('nada') 
        pass
    try:
        
        browser.find_element_by_link_text('See more posts').click()	 
    except NoSuchElementException: 
         browser.implicitly_wait(30)
         print ('complteted')
         break
print('loopened')
