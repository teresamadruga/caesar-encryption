def caesar_cypher(char_idx, char, shift, key):
    ''' https://en.wikipedia.org/wiki/Caesar_cipher
        https://keepcoding.io/blog-frr/tutorial-cifrado-cesar-en-python/
    '''
    return key[((key.index(char) + shift) % len(key))]


def vigenere_cypher(char_idx, char, table, key):
    ''' https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
    '''
    table_item = table[char_idx % len(table)]
    shift = key.index(table_item)
    return key[((key.index(char) + shift) % len(key))]
    

def encrypt(*args):
    '''
        0 : cypher function
        1 : input
        2 : shift
        3 : key
    '''
    return ''.join([args[0](i, c, args[2], args[3]) if c in args[3] else c for (i, c) in enumerate(args[1])])