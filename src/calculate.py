"""Script that calculates the cyphered output given the input from command line."""
from cypher import caesar_cypher, encrypt, inverse_vigenere_cypher, vigenere_cypher
from parse import get_input


"""Calculate the cyphered output given the input from command line."""
args = get_input()
if args.command == "caesar":
    print(encrypt(caesar_cypher, args.prompt, args.shift, args.key))
elif args.command == "vigenere" and not args.inverse:
    print(encrypt(vigenere_cypher, args.prompt, args.shift, args.key))
elif args.command == "vigenere" and args.inverse:
    print(encrypt(inverse_vigenere_cypher, args.prompt, args.shift, args.key))
