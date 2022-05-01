import caesar
import vigenere
import vernam




def main() -> None:
    args = caesar.parse()

    
    if args.mode == "hack":
        cipher = caesar.hacker(args.text)
    if args.cipher == "caesar":
        cipher = caesar.Caesar(args.key, args.text)
    elif args.cipher == "vigenere":
        cipher = vigenere.Vigenere(args.key, args.text)
    elif args.cipher == "vernam":
        cipher = vernam.Vernam(args.key, args.text)
    print(cipher)

if __name__ == '__main__':
    main()