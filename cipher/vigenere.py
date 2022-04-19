import typing
import sys


code = input()
key = input()
alphabet = ('abcdefghijklmnopqrstuvwxyz')


def coded(code, key, ind):
    i = ind + 1
    for letter in key:
        if letter not in alphabet:
            print("Key for vigenere should be a word")
            sys.exit()
    result = []
    for el in code:
        if el in alphabet:
            el = alphabet[
                (alphabet.find(el) +
                    alphabet.find(key[i])) % len(alphabet)
                ]
            i = (i + 1) % len(key)
        result.append(el)
    return ''.join(result)


def decode(code, key, ind):
    result = []
    i = ind + 1
    for el in code:
        if el in alphabet:
            el = alphabet[
                (alphabet.find(el) -
                    alphabet.find(key[i]) + len(alphabet)) % len(alphabet)
                ]
            i = (i + 1) % len(key)
        result.append(el)
    return ''.join(result)


print(decode('code', 'back', -1))
#code odec
#key
