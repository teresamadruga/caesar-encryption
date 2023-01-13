import argparse

parser = argparse.ArgumentParser(description = 'encrypt text using caesar cypher', prog = "caesar's code", usage = '%(prog)s [options]')
parser.add_argument('-s','--shift', type = int, required = True, help='number of positions to shift the key')
args = parser.parse_args()

input = 'ezevkvveky tveklip'
key = 'abcdefghijklmnopqrstuvwxyz'

def caesar_cypher(char, shift):
    ''' https://en.wikipedia.org/wiki/Caesar_cipher
        https://keepcoding.io/blog-frr/tutorial-cifrado-cesar-en-python/
    '''
    return key[((key.index(char) + shift) % len(key))]

def decode(shift):
    return ''.join([caesar_cypher(c, shift) if c in key else c for c in input])

print(decode(args.shift))