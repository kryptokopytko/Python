import decimal as d
def vat_faktura(lista):
    sum = 0.0
    for cena in lista:
        sum += cena
    return round(sum * 23.0 / 100.0, 2)
    

def vat_paragon(lista):
    sum = 0.0
    for cena in lista:
        sum += round(cena * 23.0 / 100.0, 2)
    return round(sum, 2)

def vat_fakturaD(lista):
    sum = d.Decimal('0.0')
    for cena in lista:
        sum += d.Decimal(cena)
    return round(sum * d.Decimal('23.0') / d.Decimal('100.0'), 2)
    

def vat_paragonD(lista):
    sum = d.Decimal('0.0')
    for cena in lista:
        sum += round(d.Decimal(cena) * d.Decimal('23.0') / d.Decimal('100.0'), 2)
    return round(sum, 2)

zakupy = [0.2, 0.5, 4.59, 6]
print(vat_faktura(zakupy) == vat_paragon(zakupy))
print(vat_fakturaD(zakupy) == vat_paragonD(zakupy))
print("faktura: ", vat_faktura(zakupy), "\nparagon: ", vat_paragon(zakupy))
print("faktura z Decimal: ", vat_fakturaD(zakupy), "\nparagon z Decimal: ", vat_paragonD(zakupy))
