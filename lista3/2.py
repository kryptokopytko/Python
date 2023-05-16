import math, timeit, functools
import pandas as pd

def czy_doskonala(n):
    if n < 2:
        return False
    suma = 0
    for i in range (1, n):
        if n % i == 0:
            suma += i
    return n == suma

def doskonale_imperatywna(n):
    doskonale = []
    for i in range (2, n + 1):
        if czy_doskonala(i):
            doskonale += [i]
    return doskonale
    
def doskonale_skladana(n):
    return [i for i in range(2, n + 1) if czy_doskonala(i)]
    

def doskonale_funkcyjna(n):
    return list(filter(czy_doskonala, range(2, n + 1)))

def opakowanie_timeit(f, x):
    t = timeit.Timer(functools.partial(f, x))
    return round(t.timeit(1000), 3)
    

print("imperatywna:")
print(doskonale_imperatywna(9000))
print("skladana:")
print(doskonale_skladana(9000))
print("funkcyjna:")
print(doskonale_funkcyjna(9000))

tabelka = []

for i in range (10, 100, 10):
    tabelka += [[opakowanie_timeit(doskonale_imperatywna, i), opakowanie_timeit(doskonale_skladana, i), opakowanie_timeit(doskonale_funkcyjna, i)]]

print(pd.DataFrame(tabelka, list(range(10, 100, 10)), ["imperatywna", "skladana", "funkcyjna"]))