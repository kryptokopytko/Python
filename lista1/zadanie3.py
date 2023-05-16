import pandas as pd
def tabliczka(x1, x2, y1, y2):

    tabelka = []
    for i in range (y1, y2 + 1):
        lista = []
        for j in range  (x1, x2 + 1):
            lista.append(i * j)
        tabelka.append(lista)
    iksy = []
    for i in range (x1, x2 + 1):
        iksy.append(i)
    igreki = []
    for j in range (y1, y2 + 1):
        igreki.append(j)
    print(pd.DataFrame(tabelka, igreki, iksy))

tabliczka(-3, 5, -2, 4)

