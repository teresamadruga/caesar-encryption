"""Function that cyphers the input according to the command line arguments"""
from cypher import caesar_cypher, encrypt, inverse_vigenere_cypher, vigenere_cypher
from parse import get_input


def main():
    """Cypher the input according to the command line arguments."""
    args = get_input()
    if args.command == "caesar":
        print(encrypt(caesar_cypher, args.prompt, args.shift, args.key))
    elif args.command == "vigenere" and not args.inverse:
        print(encrypt(vigenere_cypher, args.prompt, args.shift, args.key))
    elif args.command == "vigenere" and args.inverse:
        print(encrypt(inverse_vigenere_cypher, args.prompt, args.shift, args.key))
    return 0


if __name__ == "__main__":
    main()
