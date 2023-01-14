from parse import args_parse
from cypher import caesar_cypher, vigenere_cypher, encrypt


args = args_parse()
if args.command == 'caesar':
    print(encrypt(caesar_cypher, args.input, args.shift, args.key))
elif args.command == 'vigenere':
    print(encrypt(vigenere_cypher, args.input, args.shift, args.key))