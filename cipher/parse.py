import argparse

def parse():
    parser = argparse.ArgumentParser(description="1")
    parser.add_argument('--cipher', dest="cip")
    parser.add_argument('--key', dest="key", type=str)
    parser.add_argument('--text-file', dest='text')
    parser.add_argument('--input-file', dest='input_name')
    parser.add_argument('--output-file', dest='output_name')
    parser.add_argument('--model-file', dest='model')
    args = parser.parse_args()
    return args
