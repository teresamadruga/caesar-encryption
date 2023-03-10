"""Functions to parse this program command line arguments"""

import argparse

ALPHABETS = {
    "en": "abcdefghijklmnopqrstuvwxyz",
    "es": "abcdefghijklmnñopqrstuvwxyz"}


def retrieve_args():
    """Parses command line arguments"""
    parser = argparse.ArgumentParser(
        description="encrypt text using caesar cypher",
        prog="caesar's code",
        usage="%(prog)s [options]",
    )

    parser.add_argument(
        "-t", "--text", type=str, help="input text to encrypt", default=""
    )
    parser.add_argument(
        "-f", "--filename", type=str,
        help="path of file with input text to encrypt"
    )
    parser.add_argument(
        "-a",
        "--alphabet",
        type=str,
        required=True,
        help="alphabet used as key",
        default="en",
    )

    cypher_type = parser.add_subparsers(dest="command")
    caesar = cypher_type.add_parser("caesar")
    caesar.add_argument(
        "-s",
        "--shift",
        type=int,
        required=True,
        help="number of positions to shift the key",
    )
    vigenere = cypher_type.add_parser("vigenere")
    vigenere.add_argument(
        "-vt",
        "--vigenere_table",
        type=str,
        required=True,
        help="key phrase, where each character indicates"
        + " the number of displaced positions of shift"
        + " the alphabet(key)",
    )
    vigenere.add_argument(
        "-i",
        "--inverse",
        dest="inverse",
        default=False,
        action="store_true",
        help="option to code/decode vigenere cypher",
    )

    return parser.parse_args()


def get_input():
    '''Preprocesses the input'''
    args = retrieve_args()
    prompt = ""
    if args.text != "":
        prompt += args.text
    if args.filename is not None:
        # TODO: implement read file
        prompt += " " + args.filename
    args.prompt = prompt.lower()
    if args.command == "vigenere":
        args.shift = args.vigenere_table
    args.key = ALPHABETS[args.alphabet]

    print(f"{args.inverse = }")
    return args

