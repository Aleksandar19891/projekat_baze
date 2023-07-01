import sqlite3
from sqlite3 import Error
from Classes import *
from Functions import *

konekcija_baza = sqlite3.connect('Baza_projekat.db')
cursor = konekcija_baza.cursor()

tabela_konobar = '''CREATE TABLE IF NOT EXISTS konobar (ime VARCHAR(20), prezime VARCHAR(20), plata INTEGER);'''
tabela_automobil = '''CREATE TABLE IF NOT EXISTS automobil (marka VARCHAR(20), boja VARCHAR(10), kubikaza INTEGER);'''
tabela_mjesto = '''CREATE TABLE IF NOT EXISTS mjesto (lokacija VARCHAR(20), br_mjesta INTEGER, pusenje VARCHAR(20));'''
tabela_hrana = '''CREATE TABLE IF NOT EXISTS hrana (ukus VARCHAR(100), cijena INTEGER, vrijeme INTEGER);'''

cursor.execute(tabela_konobar)
cursor.execute(tabela_automobil)
cursor.execute(tabela_mjesto)
cursor.execute(tabela_hrana)

update()
select()
