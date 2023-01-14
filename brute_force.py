from parse import args_parse
from cypher import caesar_cypher, vigenere_cypher, encrypt


args = args_parse()
if args.command == 'caesar':
    for i in range(len(args.key)):
        print(str(i) + ' ' + encrypt(caesar_cypher, args.input, i, args.key))