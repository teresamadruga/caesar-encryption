import argparse

alphabets = {
    'en' : 'abcdefghijklmnopqrstuvwxyz',
    'es' : 'abcdefghijklmnñopqrstuvwxyz'
}

parser = argparse.ArgumentParser(description = 'encrypt text using caesar cypher', prog = "caesar's code", usage = '%(prog)s [options]')
parser.add_argument('-t','--text', type=str, help='input text to encrypt', default='')
parser.add_argument('-s','--shift', type = int, required = True, help='number of positions to shift the key')
parser.add_argument('-k','--key', type = str, required = True, help='alphabet used as key', default='en')
args = parser.parse_args()

# input = 'ezevkvveky tveklip'


def caesar_cypher(char, shift, key):
    ''' https://en.wikipedia.org/wiki/Caesar_cipher
        https://keepcoding.io/blog-frr/tutorial-cifrado-cesar-en-python/
    '''
    return key[((key.index(char) + shift) % len(key))]

def decode(input, shift, key):
    return ''.join([caesar_cypher(c, shift, key) if c in key else c for c in input])

print(decode(args.text, args.shift, alphabets[args.key]))