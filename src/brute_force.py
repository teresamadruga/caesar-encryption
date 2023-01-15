'''Brute force script that prints all possible caesar encryptions of a prompt given an alphabet'''
from parse import args_parse
from cypher import caesar_cypher, encrypt

# applies caesar cypher to the input with all possible variations in the alphabet
args = args_parse()
if args.command == 'caesar':
    for i in range(len(args.key)):
        print(str(i) + ' ' + encrypt(caesar_cypher, args.prompt, i, args.key))
