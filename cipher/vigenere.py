import sys

class Vigener:
    code = input()
    key = input()
    alphabet = ('abcdefghijklmnopqrstuvwxyz')


def coded(self, code, key, ind):
    i = ind + 1
    for letter in key:
        if letter not in self.alphabet:
            print("Key for vigenere should be a word")
            sys.exit()
    result = []
    for el in code:
        if el in self.alphabet:
            el = self.alphabet[
                (self.alphabet.find(el) +
                    self.alphabet.find(key[i])) % len(self.alphabet)
                ]
            i = (i + 1) % len(key)
        result.append(el)
    return ''.join(result)


def decode(self, code, key, ind):
    result = []
    i = ind + 1
    for el in code:
        if el in self.alphabet:
            el = self.alphabet[
                (self.alphabet.find(el) -
                    self.alphabet.find(key[i]) + len(self.alphabet)) % len(self.alphabet)
                ]
            i = (i + 1) % len(key)
        result.append(el)
    return ''.join(result)


print(decode('code', 'back', -1))
#code odec
#key
