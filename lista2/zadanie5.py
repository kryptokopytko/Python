def kompresja(tekst):
    lista = []
    znak = [1, tekst[0]]
    for i in range (1, len(tekst)):
        if (znak[1] == tekst[i]):
            znak[0] += 1
        else:
            lista.append(znak)
            znak = [1, tekst[i]]
    lista.append(znak)
    return lista


def dekompresja(tekst_skompresowany):
    tekst = ""
    for znak in tekst_skompresowany:
        for i in range (0, znak[0]):
            tekst += znak[1]
    return tekst


print(kompresja("suuuuuperanckoooo, aaaaa, wspaniale"))
print(dekompresja(kompresja("suuuuuperanckoooo, aaaaa, wspaniale")))
print(dekompresja(kompresja("Często latami hartują się dzieła, zanim dojrzeją do pełnej wzniosłości.")))
#dzielo literackie: https://lektury.gov.pl/lektura/faust
