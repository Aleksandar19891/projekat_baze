class Konobar:
    def __init__(self, ime, prezime, plata):
        self.ime = ime
        self.prezime = prezime
        self.plata = plata

    def __str__(self):
        return f'{self.ime} {self.prezime} ima {self.plata} platu'

class Automobil:
    def __init__(self, marka, boja, kubikaza):
        self.marka = marka
        self.boja = boja
        self.kubikaza = kubikaza

    def __str__(self):
        return f'Automobil {self.marka} {self.boja} je {self.kubikaza} za dostavu'

class Mjesto:
    def __init__(self, lokacija, br_mjesta, pusenje):
        self.lokacija = lokacija
        self.br_mjesta = br_mjesta
        self.pusenje = pusenje

    def __str__(self):
        return f'{self.lokacija} je uvijek slobodan, a za {self.br_mjesta} i {self.pusenje} su potrebne rezervacije unaprijed'

class Hrana:
    def __init__(self, ukus, cijena, vrijeme):
        self.ukus = ukus
        self.cijena = cijena
        self.vrijeme = vrijeme

    def __str__(self):
        return f'Preporuka za predjelo je uvijek {self.ukus},{self.cijena} ispod saca za glavno jelo i topla preporuka za dezert{self.vrijeme}'



