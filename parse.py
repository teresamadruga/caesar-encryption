import argparse

ALPHABETS = {
    'en' : 'abcdefghijklmnopqrstuvwxyz',
    'es' : 'abcdefghijklmnñopqrstuvwxyz'
}

# input = 'ezevkvveky tveklip'

def args_parse():
    parser = argparse.ArgumentParser(description = 'encrypt text using caesar cypher', prog = "caesar's code", usage = '%(prog)s [options]')
    parser.add_argument('-t','--text', type=str, help='input text to encrypt', default='')
    parser.add_argument('-s','--shift', type = int, required = True, help='number of positions to shift the key')
    parser.add_argument('-a','--alphabet', type = str, required = True, help='alphabet used as key', default='en')
    args = parser.parse_args()
    input = args.text.lower()
    args.input = input
    args.key = ALPHABETS[args.alphabet]
    return args