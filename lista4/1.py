from itertools import *
import operator

def cryptarithm(word1, word2, word3, operator):
    letters = set(word1).union(set(word2), set(word3))
    digits = list(range(0, 9))
    perms = permutations(digits, len(letters))
    for values in perms:
        lletters = list(letters)
        res = {lletters[i]: values[i] for i in range(len(lletters))}
        mapped1 = word_to_num(word1, res)
        mapped2 = word_to_num(word2, res)
        mapped3 = word_to_num(word3, res)
        if eat_operator(operator, mapped1, mapped2) == mapped3:
            yield res
    
def word_to_num(word, dictionary):
    return int(''.join(map(str, [dictionary[l] for l in word])))

def eat_operator(op, a, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '/' or op == ':':
        return a / b
    if op == '*':
        return a * b


gen = cryptarithm("KIOTO", "OSAKA", "TOKIO", '+')
for i in gen:
    print(i)
    
print()

gen = cryptarithm("SEND", "MORE", "MONEY", '+')
for i in gen:
    print(i)
