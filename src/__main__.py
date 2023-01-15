"""Function that cyphers the input according to the command line arguments"""
from cypher import caesar_cypher, encrypt, vigenere_cypher
from parse import get_input


def main():
    """Cypher the input according to the command line arguments."""
    args = get_input()
    if args.command == "caesar":
        print(encrypt(caesar_cypher, args.prompt, args.shift, args.key))
    elif args.command == "vigenere":
        print(encrypt(vigenere_cypher, args.prompt, args.shift, args.key))
    return 0


main()
