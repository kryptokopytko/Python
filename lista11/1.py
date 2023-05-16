from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, create_engine, Boolean
from sqlalchemy.orm import relationship, sessionmaker, validates
import sys, getopt, datetime
Base = declarative_base()

engine = create_engine("sqlite:///ksiazki.db", echo=True)
Session = sessionmaker(bind=engine)
sesja = Session()

class Znajomy(Base):
    __tablename__ = "Znajomi"
    id = Column(Integer, primary_key = True)
    imie = Column(String(20), nullable = False)
    wiek = Column(Integer, default = 18)
    email = Column(String(30), nullable = False)

    ksiazki = relationship("Ksiazka", back_populates = "znajomy")

    @validates("email")
    def validate_email(self, key, value):
        assert '@' in value
        return value
    def print(self):
        print("Imie:", self.imie, "   wiek:", self.wiek, "   email:", self.email, "   id:", self.id)

class Ksiazka(Base):
    __tablename__ = "Ksiazki"
    id = Column(Integer, primary_key = True)
    autor = Column(String(40), nullable = False)
    tytul = Column(String(50), nullable = False)
    rok = Column(Integer, default = 2022)
    gatunek = Column(String(20))

    znajomy_id = Column(Integer, ForeignKey("Znajomi.id"))
    znajomy = relationship("Znajomy", back_populates = "ksiazki")

    wydawnictwo_id = Column(Integer, ForeignKey("Wydawnictwa.id"))
    wydawnictwo = relationship("Wydawnictwo", back_populates = "ksiazki")

    def print(self):
        print("Autor:", self.autor, "  tytul:", self.tytul, "  rok:", self.rok, "  gatunek:", self.gatunek)
    @validates(rok)
    def validate_rok(self, key, value):
        assert value > 0
        return value

class Wydawnictwo(Base):
    __tablename__ = "Wydawnictwa"
    id = Column(Integer, primary_key = True)
    nazwa = Column(String(40), nullable = False)
    ksiazki = relationship("Ksiazka", back_populates = "wydawnictwo")

    @validates(nazwa)
    def validate_nazwa(self, key, value):
        assert value != ""
        return value

Base.metadata.create_all(engine)

def wypisz_ksiazki():
    resultK = sesja.query(Ksiazka).all()

    print("\nKsiazki:")
    for row in resultK:
        print ("Tytul: ",row.tytul, "Autor:",row.autor)
def wypisz_znajomych():
    resultZ = sesja.query(Znajomy).all()

    print("\nZnajomi:")
    for row in resultZ:
        print ("Imie: ",row.imie, "email:",row.email)

def wypisz_wypozyczenia():
    for z, k in sesja.query(Znajomy, Ksiazka).filter(Znajomy.id == Ksiazka.znajomy_id).all():
        print ("imie znajomego: {}, tytul ksiazki: {}, autor: {}, ID znajomego: {}, ID ksiazki: {}.".format(z.imie, k.tytul, k.autor, z.id, k.id))

def wypozycz(znajomy, ksiazka):
    znajomy.ksiazki.append(ksiazka)
    ksiazka.znajomy_id = znajomy.id
    sesja.commit()


def oddaj(znajomy, ksiazka):
    znajomy.ksiazki.remove(ksiazka)
    ksiazka.znajomy_id = None
    sesja.commit()


def nowa_ksiazka(tytul, autor, rok, gatunek):
    nowa = Ksiazka(tytul = tytul, autor = autor, rok = rok, gatunek = gatunek)
    sesja.add(nowa)
    sesja.commit()
    return nowa

def nowy_znajomy(imie, wiek, email):
    nowa = Znajomy(imie = imie, wiek = wiek, email = email)
    sesja.add(nowa)
    sesja.commit()
    return nowa

def wykonaj_polecenia():
    argv = sys.argv[1:]
    for i in range (0, len(argv)):
        if (argv[i] == "dodajz"):
            nowy_znajomy(argv[i + 1], argv[i + 2], argv[i + 3])
            i += 3
        elif (argv[i] == "dodajk"):
            nowa_ksiazka(argv[i + 1], argv[i + 2], argv[i + 3], argv[i + 4])
            i += 4
        elif (argv[i] == "wypisz"):
            wypisz_wypozyczenia()
        elif (argv[i] == "oddaj"):
            for z, k in sesja.query(Znajomy, Ksiazka).filter(Znajomy.imie == argv[i + 1] and Ksiazka.tytul == argv[i + 2] and Znajomy.id == Ksiazka.znajomy_id).all():
                oddaj(z, k)
            i += 2
        elif (argv[i] == "wypozycz"):
            for z, k in sesja.query(Znajomy, Ksiazka).filter(Znajomy.imie == argv[i + 1] and Ksiazka.tytul == argv[i + 2]).all():
                wypozycz(z, k)
            i += 2
        elif (argv[i] == "--help"):
            print("dodajz(imie, wiek, email) - dodaj znajomego\ndodajk(tytul, autor, rok, gatunek) - dodaj znajomego\nwypisz() - wypisz wypozyczenia\ndodaj(imie, tytul)\nwypozycz(imie, tytul)")



peach = Ksiazka(autor = "Jimmy Shive Overly", tytul = "The width of the peach", rok = 2015, gatunek = "wojenne")
metal = Ksiazka(autor = "Brandon Sanderson", tytul = "Zaginiony metal", gatunek = "fantastyka")
oslona = Ksiazka(autor = "Jojo Moyes", tytul = "Pod oslona deszczu")
taniec = Ksiazka(autor = "George R. R. Martin", tytul = "Taniec ze smokami")
jasia = Znajomy(imie = "Jasia", email = "dsf@fds", ksiazki = [oslona])
basia = Znajomy(imie = "Basia", wiek = 20, email = "basiunia@gmail.com", ksiazki = [peach, metal])

def add_test():    
    sesja.add_all([peach, metal, taniec, oslona])
    sesja.add_all([basia, jasia])
    sesja.commit()

def test():
    add_test()
    wypozycz(basia, taniec)
    n = nowa_ksiazka("Ta, ktora stala sie sloncem", "Shelly Parker-Chan", 2022, "fantastyka")
    ton = nowa_ksiazka("Ton", "Marta Kisiel", 2018, "fantastyka")
    wypozycz(jasia, n)

    wypisz_wypozyczenia()

wykonaj_polecenia()