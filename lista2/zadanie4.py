import random
def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    slowo = ""
    zdanie = []
    for i in tekst:
        if i == ' ':
            if len(slowo) <= dl_slowa:
                zdanie.append(slowo + ' ') 
            slowo = ""
        else:
            slowo += i
    if len(slowo) - 1 <= dl_slowa: # zakladajac ze zdanie konczy sie kropka
       zdanie.append(slowo) 
    while(len(zdanie) > liczba_slow):
        zdanie.pop(random.randrange(len(zdanie)))
    wynik = ""
    for i in zdanie:
        wynik += i
    return wynik

print(uprosc_zdanie("Podział peryklinalny inicjałów wrzecionowatych kambium charakteryzuje się ścianą podziałową inicjowaną w płaszczyźnie maksymalnej.", 10, 5))
#dzielo literackie: https://lektury.gov.pl/lektura/faust
print(uprosc_zdanie("Często latami hartują się dzieła, zanim dojrzeją do pełnej wzniosłości.", 5, 2))