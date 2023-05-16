def is_palindrom(text):
    text = ''.join(filter(str.isalpha, text))
    text = text.lower()
    length = len(text)
    for i in range (0, length):
        if (text[i] != text[length - i - 1]):
            return False
    return True


print(is_palindrom("Ah, Mr. Secretary! /Mr. Burr, sir/Did you hear the news about good old General Mercer?/No/You know Claremont street?/Yeah/They renamed it after him/The Mercer legacy is secure/Sure/And all he had to do is die/And that's a lot less work!/We ought to give it a try"))
print(is_palindrom("A man, a plan, a canal—Panama!"))
print(is_palindrom("Eine güldne, gute Tugend: Lüge nie!"))
print(is_palindrom("Míč omočím."))
print(is_palindrom("Kobyła ma mały bok."))
