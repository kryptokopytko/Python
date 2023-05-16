from itertools import *

class Formula:
    def tautologia(self):
        perms = permutations([0, 1], len(self.zmienne()))
        for values in perms:
            slownik = {self.zmienne()[i]: values[i] for i in range(len(self.zmienne()))}
            if self.oblicz(slownik) == False:
                return False
        return True
    def wlasciwosci(self, podstawienia):
        print("postac infiksowa: ", self)
        print("wartosc: ", self.oblicz(podstawienia))
        print("Zmienne: ", self.zmienne())
        print("Czy tautologia: ", self.tautologia())
        print()
    def __add__(self, fi):
        return Alternatywa(self, fi)
    def __mul__(self, fi):
        return Koniunkcja(self, fi)


class Zmienna(Formula):
    def __init__(self, nazwa):
        self.nazwa = nazwa
    def oblicz(self, podstawienia):
        return podstawienia[self.nazwa]
    def __str__(self):
        return self.nazwa
    def zmienne(self):
        return [self.nazwa]
    def uprosc(self):
        return self

    
class Alternatywa(Formula):
    def __init__(self, fi, psi):
        self.lewa = fi
        self.prawa = psi
    def oblicz(self, podstawienia):
        return self.lewa.oblicz(podstawienia) or self.prawa.oblicz(podstawienia)
    def __str__(self):
        return " ("+ self.lewa.__str__()+ " ∨ "+ self.prawa.__str__()+ ") "
    def zmienne(self):
        return list(set(self.lewa.zmienne() + self.prawa.zmienne()))
    def uprosc(self):
        if (isinstance(self.prawa, Stala) and self.prawa.wartosc == True) or (isinstance(self.lewa, Stala) and self.lewa.wartosc == True):
            return Stala(True)
        if (isinstance(self.prawa, Stala) and self.prawa.wartosc == False) and (isinstance(self.lewa, Stala) and self.lewa.wartosc == False):
            return Stala(False)
        return self
    
class Koniunkcja(Formula):
    def __init__(self, fi, psi):
        self.lewa = fi
        self.prawa = psi
    def oblicz(self, podstawienia):
        return self.lewa.oblicz(podstawienia) and self.prawa.oblicz(podstawienia)
    def __str__(self):
        return " ("+ self.lewa.__str__()+ " ∧ "+ self.prawa.__str__()+ ") " 
    def zmienne(self):
        return list(set(self.lewa.zmienne() + self.prawa.zmienne()))
    def uprosc(self):
        if (isinstance(self.prawa, Stala) and self.prawa.wartosc == False) or (isinstance(self.lewa, Stala) and self.lewa.wartosc == False):
            return Stala(False)
        if (isinstance(self.prawa, Stala) and self.prawa.wartosc == True) and (isinstance(self.lewa, Stala) and self.lewa.wartosc == True):
            return Stala(True)
        return self

class Negacja(Formula):
    def __init__(self, fi):
        self.formula = fi
    def oblicz(self, podstawienia):
        return not(self.formula.oblicz(podstawienia))
    def __str__(self):
        return " ¬("+ self.formula.__str__()+ ") "
    def zmienne(self):
        return self.formula.zmienne()
    def uprosc(self):
        if isinstance(self.formula, Stala) and self.formula.wartosc == False:
            return Stala(True)
        if isinstance(self.formula, Stala) and self.formula.wartosc == True:
            return Stala(False)
        return self


class Stala(Formula):
    def __init__(self, wartosc):
        self.wartosc = wartosc
    def oblicz(self, podstawienia):
        return self.wartosc
    def __str__(self):
        return str(self.wartosc)
    def zmienne(self):
        return []
    def uprosc(self):
        return self
    
class ZlalLiczbaZmiennych(Exception):
    "liczba zmiennych w formule i w podstawieniach sie nie zgadzaja"
    pass

podstawienia = {
    "x" : True,
    "y" : False
}

podstawienia2 = {
    "x" : True
}

zdanie = Alternatywa(Negacja(Zmienna("x")), Koniunkcja(Stala(True), Zmienna("y")))
zdanie2 = Alternatywa(Negacja(Zmienna("x")), Zmienna("x"))
zdanie3 = Negacja(Zmienna("x") + Zmienna("y")) * Stala(False)

if len(zdanie.zmienne()) != len(podstawienia):
    raise ZlalLiczbaZmiennych
if len(zdanie2.zmienne()) != len(podstawienia2):
    raise ZlalLiczbaZmiennych
if len(zdanie3.zmienne()) != len(podstawienia):
    raise ZlalLiczbaZmiennych

try:
    zdanie.wlasciwosci(podstawienia)
    zdanie2.wlasciwosci(podstawienia2)
    zdanie3.wlasciwosci(podstawienia)
except KeyError:
    print("Brak przypisania wartosci zmiennej")
else:
    print("uproszczenie: ", zdanie3.uprosc())
