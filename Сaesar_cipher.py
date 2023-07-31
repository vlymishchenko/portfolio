import string

def Cesar(st, x):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    stnew = ''
    for i in st:
        pos = alphabet.find(i.lower())
        if pos == -1:
            stnew = stnew + i
            continue
        pos = pos + x
        if pos > 25:
            pos = pos % 26
        stnew = stnew + alphabet[pos]
    return stnew

def CesarDecipher(string1, y):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    stnew = ''
    for i in string1:
        pos = alphabet.find(i)
        if pos == -1:
            stnew = stnew + i
            continue
        pos = pos - y
        if pos > 25:
            pos = pos % 26
        stnew = stnew + alphabet[pos]
    return stnew

text = 'q twdm gwc'

for i in range(1,26):
    print(CesarDecipher(text, i), i)
