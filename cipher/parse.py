import argparse
import caesar
import vigenere
import vernam

def parse():
    """Ввод параметров из консоли"""
    parser = argparse.ArgumentParser(description="encrypt incoming information")
    parser.add_argument('-c', '--cipher', type=str, dest="choice_of_encryption")
    parser.add_argument('-k', '--key', dest="key", type=str)
    parser.add_argument('-t', '--type', dest='type')
    parser.add_argument('-inp', '--input-file', dest='input_name')
    parser.add_argument('-out', '--output-file', dest='output_name')
    parser.add_argument('-fa', '--freq-analysis', dest='freq-analysis')
    args = parser.parse_args()

    dict = {
        'caesar' : caesar.Caesar,
        'vigenere' : vigenere.Vigener,
        'vernam' : vernam.Vernam
    }
    with open(args.inp, 'r') as inp:
        text_read = inp.read()
        if args.fa:
            line = text_read
            f_write = open(args.output, 'w')
            obj = caesar.Caesar()
            f_write.write(obj.caesar1(line, args.key))
            f_write.close()
        elif args.choice_of_encryption == 'code':
            line = text_read
            f_write = open(args.output, 'w')
            obj = dict[args]
            f_write.write(obj.code_this(line, args.key))
            f_write.close()
        elif args.choice_of_encryption == 'decode':
            line = text_read
            f_write = open(args.output, 'w')
            obj = caesar.Caesar()
            f_write.write(obj.caesar2(line, args.key))
            f_write.close()
