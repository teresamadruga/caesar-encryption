# https://keepcoding.io/blog-frr/tutorial-cifrado-cesar-en-python/
import argparse

parser = argparse.ArgumentParser(description = 'encrypt text using caesar cypher', prog = "caesar's code", usage = '%(prog)s [options]')
parser.add_argument('-k','--key', type = int, required = True, help='private key')
args = parser.parse_args()

input = 'ezevkvveky tveklip'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

k=args.key

decypher = ''

for char in input:
    if char in alphabet:
        new_index = (alphabet.index(char) + k) % len(alphabet)
        decypher += alphabet[new_index]
    else:
        decypher += char


print(decypher)