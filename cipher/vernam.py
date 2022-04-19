class Vernam:
    def vernam1(self, code, key) -> str:
        out = []
        for i in range(0, len(code)):
            out.append(chr(ord(code[i]) ^ ord(key[i])))
        return ''.join(out)


    def vernam2(self, code, key) -> str:
        out = []
        for i in range(0, len(code)):
            out.append(chr(ord(code[i]) ^ ord(key[i])))
        return ''.join(out)
