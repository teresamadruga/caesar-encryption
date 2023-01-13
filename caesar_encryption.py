# https://keepcoding.io/blog-frr/tutorial-cifrado-cesar-en-python/

input = 'ezevkvveky tveklip'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

k=9
decypher = ''

for char in input:
    if char in alphabet:
        new_index = (alphabet.index(char) + k) % len(alphabet)
        decypher += alphabet[new_index]
    else:
        decypher += char


print(decypher)