alphabet = 'abcdefghijklmnopqrstuvwxyz'
#choice = int(input())
def caesar1(code, key):
        #code = input()
        #key = int(input())
        val_low = code.lower()
        decoded = ''

        for letter in val_low:
            position = alphabet.find(letter)
            new_position = (position + key) % len(alphabet)
            if letter in alphabet:
                decoded = decoded + alphabet[new_position]
            else:
                decoded = decoded + letter
        return decoded
def caesar2(code, key):
        #code = input()
        #key = int(input())
        val_low = code.lower()
        decoded = ''

        for letter in val_low:
            position = alphabet.find(letter)
            new_position = (position - key + len(alphabet)) % len(alphabet)
            if letter in alphabet:
                decoded = decoded + alphabet[new_position]
            else:
                decoded = decoded + letter
        return decoded
caesar1("abcdef", 1)
