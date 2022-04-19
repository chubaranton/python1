def vernam1(code, key) -> str:
    out = []
    for i in range(0, len(code)):
        out.append(chr(ord(code[i]) ^ ord(key[i])))
    return ''.join(out)


def vernam2(code, key) -> str:
    out = []
    for i in range(0, len(code)):
        out.append(chr(ord(code[i]) ^ ord(key[i])))
    return ''.join(out)
