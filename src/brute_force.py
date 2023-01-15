"""Brute force script that prints all possible caesar encryptions
of a prompt given an alphabet"""
from cypher import caesar_cypher, encrypt
from parse import get_input


def brute_force():
    '''Applies caesar cypher to the input
    with all possible shift variations in the alphabet
    '''
    args = get_input()
    if args.command == "caesar":
        for i in range(len(args.key)):
            print(str(i) + " " + encrypt(
                caesar_cypher, args.prompt, i, args.key))


brute_force()
