import math, timeit, functools
import pandas as pd

def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range (2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def pierwsze_imperatywna(n):
    pierwsze = []
    for i in range (2, n + 1):
        if czy_pierwsza(i):
            pierwsze += [i]
    return pierwsze
    
def pierwsze_skladana(n):
    return [i for i in range(2, n + 1) if czy_pierwsza(i)]
    

def pierwsze_funkcyjna(n):
    return list(filter(czy_pierwsza, range(2, n + 1)))

def opakowanie_timeit(f, x):
    t = timeit.Timer(functools.partial(f, x))
    return round(t.timeit(1000), 3)
    

print("imperatywna:")
print(pierwsze_imperatywna(31))
print("skladana:")
print(pierwsze_skladana(31))
print("funkcyjna:")
print(pierwsze_funkcyjna(31))

tabelka = []

for i in range (10, 100, 10):
    tabelka += [[opakowanie_timeit(pierwsze_imperatywna, i), opakowanie_timeit(pierwsze_skladana, i), opakowanie_timeit(pierwsze_funkcyjna, i)]]

print(pd.DataFrame(tabelka, list(range(10, 100, 10)), ["imperatywna", "skladana", "funkcyjna"]))