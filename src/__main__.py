'''Function that cyphers the input according to the command line arguments'''
from parse import args_parse
from cypher import caesar_cypher, vigenere_cypher, encrypt


def main():
    ''' Cypher the input according to the command line arguments.
    '''
    args = args_parse()
    if args.command == 'caesar':
        print(encrypt(caesar_cypher, args.prompt, args.shift, args.key))
    elif args.command == 'vigenere':
        print(encrypt(vigenere_cypher, args.prompt, args.shift, args.key))
    return 0


main()
