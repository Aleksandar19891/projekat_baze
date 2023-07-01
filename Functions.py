import sqlite3
from Classes import *
# FunctionDelete


def delete():
    tabela = int(input('Kojoj tabeli zelite pristup: Konobar-1, Automobil-2, Mjesto-3, Hrana-4? '))

    if tabela == 1:
        konekcija = sqlite3.connect('Baza_projekat.db')
        cursor = konekcija.cursor()
        delete = input('Unesite vrijednost kolone:')
        kolona = input("Unesite kolonu: ")
        naredba = f'''DELETE FROM konobar WHERE {kolona} = '{delete}' '''
        cursor.execute(naredba)
        konekcija.commit()

    elif tabela == 2:
        konekcija = sqlite3.connect('Baza_projekat.db')
        cursor = konekcija.cursor()
        delete = input('Unesi vrijednost kolone: ')
        kolona = input("Unesite kolonu")
        naredba = f'''DELETE FROM automobil WHERE {kolona} = '{delete}' '''
        cursor.execute(naredba)
        konekcija.commit()

    elif tabela == 3:
        konekcija = sqlite3.connect('Baza_projekat.db')
        cursor = konekcija.cursor()
        delete = input('Unesite vrijednost kolone: ')
        kolona = input("Unesite kolonu")
        naredba = f'''DELETE FROM mjesto WHERE {kolona} = '{delete}' '''
        cursor.execute(naredba)
        konekcija.commit()

    elif tabela == 4:
        konekcija = sqlite3.connect('Baza_projekat.db')
        cursor = konekcija.cursor()
        delete = input('Unesite vrijednost kolone: ')
        kolona = input("Unesite kolonu: ")
        naredba = f'''DELETE FROM hrana WHERE {kolona} = '{delete}' '''
        cursor.execute(naredba)
        konekcija.commit()


# FunctionSelect


def select():
    konekcija = sqlite3.connect('Baza_projekat.db')
    tabela = int(input('Kojoj tabeli zelis da pristupis:  Konobar-1, Automobil-2, Mjesto-3, Hrana-4'))

    if tabela == 1:
        naredba = '''SELECT * FROM konobar'''
        cursor = konekcija.cursor()
        cursor.execute(naredba)
        rezultat = cursor.fetchall()
        for i in rezultat:
            print(i)

    elif tabela == 2:
        naredba = '''SELECT * FROM automobil'''
        cursor = konekcija.cursor()
        cursor.execute(naredba)
        rezultat = cursor.fetchall()
        for i in rezultat:
            print(i)

    elif tabela == 3:
        naredba = '''SELECT * FROM mjesto'''
        cursor = konekcija.cursor()
        cursor.execute(naredba)
        rezultat = cursor.fetchall()
        for i in rezultat:
            print(i)

    elif tabela == 4:
        naredba = '''SELECT * FROM hrana'''
        cursor = konekcija.cursor()
        cursor.execute(naredba)
        rezultat = cursor.fetchall()
        for i in rezultat:
            print(i)

# FunctionInsert

def insert():
    tabela = int(input("Kojoj tabeli zelite pristup? Konobar-1, Automobil-2, Mjesto-3, Hrana-4"))
    if tabela == 1:
        n = int(input('Koliko konobara zelite?'))
        while n > 0:
            konekcija = sqlite3.connect("Baza_projekat.db")
            def args_Konobar():
                ime = input("Ime konobara?")
                prezime = input("Prezime konobara")
                plata = int(input("Plata konobara?"))
                konobar = Konobar(ime,prezime,plata)
                return (konobar.ime, konobar.prezime, konobar.plata)
            naredba = '''INSERT INTO konobar VALUES (?,?,?);'''
            kursor = konekcija.cursor()
            kursor.execute(naredba, args_Konobar())
            konekcija.commit()
            n -= 1

    elif tabela == 2:
        n = int(input("Koliko zelite automobila"))
        while n > 0:
            konekcija = sqlite3.connect('Baza_projekat.db')
            def args_Automobil():
                marka = input("Marka automobila")
                boja = input ("Boja automobila")
                kubikaza = int(input("Koliko kubika ima auto"))
                automobil = Automobil(marka, boja, kubikaza)
                return (automobil.marka, automobil.boja, automobil.kubikaza)
            naredba = '''INSERT INTO automobil VALUES(?,?,?);'''
            kursor = konekcija.cursor()
            kursor.execute(naredba, args_Automobil())
            konekcija.commit()
            n -= 1

    elif tabela == 3:
        n = int(input('Koliko mjesta zelite rezervisati?'))
        while n > 0:
            konekcija = sqlite3.connect('Baza_projekat.db')
            def args_Mjesto():
                lokacija = input('Lokacija stola')
                br_mjesta = int(input("Broj mjesta za stolom"))
                pusenje = input("Pusacki/Nepusacki")
                mjesto = Mjesto(lokacija, br_mjesta, pusenje)
                return (mjesto.lokacija, mjesto.br_mjesta, mjesto.pusenje)
            naredba = '''INSERT INTO mjesto VALUES(?,?,?);'''
            kursor = konekcija.cursor()
            kursor.execute(naredba, args_Mjesto())
            konekcija.commit()
            n -= 1

    elif tabela == 4:
        n = int(input('Koliko hrane zelite da dodate na meni'))
        while n > 0:
            konekcija = sqlite3.connect('Baza_projekat.db')
            def args_Hrana():
                ukus = input('Da li je slano ili slatko')
                cijena = int(input('Koja je cijena hrane'))
                vrijeme = int(input('Vrijeme spremanja?'))
                hrana = Hrana(ukus, cijena, vrijeme)
                return (hrana.ukus, hrana.cijena, hrana.vrijeme)

            naredba = '''INSERT INTO hrana VALUES(?,?,?);'''
            kursor = konekcija.cursor()
            kursor.execute(naredba, args_Hrana())
            konekcija.commit()
            n -= 1

# FunctionUpdate
def update():
    konekcija = sqlite3.connect("Baza_projekat.db")
    kursor = konekcija.cursor()
    tabela = input("Tabela")
    atribut = input("Koji bi ste atribut azurirali")
    nova_verzija = input("Nova verzija tog atributa je: ")
    pretrarga = input("Atribut za pretragu: ")
    vr_pretrage = input("Vrijednost atributa za pretragu: ")
    komanda = f'''UPDATE {tabela} SET {atribut} = "{nova_verzija}" WHERE {pretrarga} = "{vr_pretrage}"  '''
    kursor.execute(komanda)
    konekcija.commit()











