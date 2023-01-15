"""Brute force script that prints all possible caesar encryptions
of a prompt given an alphabet"""
from cypher import caesar_cypher, encrypt
from parse import args_parse

# applies caesar cypher to the input
# with all possible variations in the alphabet
args = args_parse()
if args.command == "caesar":
    for i in range(len(args.key)):
        print(str(i) + " " + encrypt(caesar_cypher, args.prompt, i, args.key))
