def pierwiastek(n):
    i = 0
    while n >= 0:
        n -= 2 * i + 1
        i += 1
    return i - 1

for i in range (1, 100):
    print("i:", i, "pierwiastek:", pierwiastek(i))