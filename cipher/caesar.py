eng_freq = {
    'a': 8.17, 'b': 1.4, 'c': 2.78, 'd': 4.25, 'e': 12.7, 'f': 2.23, 'g': 2.02, 'h': 6.09,
    'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93,
    'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15,
    'y': 1.97, 'z': 0.07
}
alphabet = 'abcdefghijklmnopqrstuvwxyz'


# choice = int(input())
class Caesar:
    def caesar1(self, code, key):
        # code = input()
        # key = int(input())

        decoded = ''

        for letter in code:
            position = alphabet.find(letter)
            new_position = (position + key) % len(alphabet)
            if letter in alphabet:
                decoded = decoded + alphabet[new_position]
            else:
                decoded = decoded + letter
        return decoded

    def caesar2(self, code, key):
        # code = input()
        # key = int(input())
        decoded = ''

        for letter in code:
            position = alphabet.find(letter)
            new_position = (position - key + len(alphabet)) % len(alphabet)
            if letter in alphabet:
                decoded = decoded + alphabet[new_position]
            else:
                decoded = decoded + letter
        return decoded

    def fhack(self, break_text):
        freq = sum([abs(eng_freq[l] - 100 * (break_text.count(l) / len(break_text))) for l in break_text])
        return freq

    def hack(self, message):
        MyList = []
        for i in range(26):
            MyList.append(self.fhack(self.caesar2(message, i)))
        i = MyList.index(min(MyList))
        return self.caesar2(message, i)
