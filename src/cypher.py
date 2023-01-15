'''Functions to encrypt'''

def caesar_cypher(char_idx, char, shift, key):
    ''' Cyphers a character with caesar cypher.
        TODO: args
        The character is encrypted by displacing its position
        in an alphabet(key) by a value(shift).
        https://en.wikipedia.org/wiki/Caesar_cipher
        https://keepcoding.io/blog-frr/tutorial-cifrado-cesar-en-python/
    '''
    return key[((key.index(char) + shift) % len(key))]


def vigenere_cypher(char_idx, char, table, key):
    ''' Cyphers a character with vigenere cypher, a variant of caesar cypher.
        TODO: args
        First it calculates the displacement value(shift), given the character
        position and a key phrase.
        Then the character is encrypted by displacing its position
        in an alphabet(key) by the displacement value(shift).
        https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
    '''
    shift = key.index(table[char_idx % len(table)])
    return key[((key.index(char) + shift) % len(key))]


def encrypt(cypher, prompt, shift, key):
    ''' Cyphers a prompt with caesar or vigenere code.
        TODO: args
    '''
    return ''.join([cypher(i, c, shift, key) if c in key else c for (i, c) in enumerate(prompt)])
