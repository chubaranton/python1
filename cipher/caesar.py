import Global

# choice = int(input())
class Caesar:
    def caesar1(self, code, key):
        """Происходит шифрование по шифру Цезаря"""
        # code = input()
        # key = int(input())

        decoded = ''

        for letter in code:
            position = Global.alphabet.find(letter)
            new_position = (position + key) % len(Global.alphabet)
            if letter in Global.alphabet:
                decoded = decoded + Global.alphabet[new_position]
            else:
                decoded = decoded + letter
        return decoded

    def caesar2(self, code, key):
        """Происходит расшифрование по шифру Цезаря"""
        # code = input()
        # key = int(input())
        decoded = ''

        for letter in code:
            position = Global.alphabet.find(letter)
            new_position = (position - key + len(Global.alphabet)) % len(Global.lphabet)
            if letter in Global.alphabet:
                decoded = decoded + Global.alphabet[new_position]
            else:
                decoded = decoded + letter
        return decoded

    def fhack(self, break_text):
        """Нахождение метрик"""
        freq = sum([abs(Global.eng_freq[l] - 100 * (break_text.count(l) / len(break_text))) for l in break_text])
        return freq

    def hack(self, message):
        """Взлом шифра цезаря с помощью найденых метрик"""
        MyList = []
        for i in range(Global.const1):
            MyList.append(self.fhack(self.caesar2(message, i)))
        i = MyList.index(min(MyList))
        return self.caesar2(message, i)