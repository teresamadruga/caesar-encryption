import argparse

ALPHABETS = {
    'en' : 'abcdefghijklmnopqrstuvwxyz',
    'es' : 'abcdefghijklmnñopqrstuvwxyz'
}

# input = 'ezevkvveky tveklip'

def args_parse():
    parser = argparse.ArgumentParser(description = 'encrypt text using caesar cypher', prog = "caesar's code", usage = '%(prog)s [options]')
    
    parser.add_argument('-t','--text', type=str, help='input text to encrypt', default='')
    parser.add_argument('-f','--filename', type=str, help='path of file with input text to encrypt', default='')
    parser.add_argument('-a','--alphabet', type = str, required = True, help='alphabet used as key', default='en')

    cypher_type = parser.add_subparsers(dest='command')
    caesar = cypher_type.add_parser('caesar')
    caesar.add_argument('-s','--shift', type = int, required = True, help='number of positions to shift the key')   
    vigenere = cypher_type.add_parser('vigenere')
    vigenere.add_argument('-vt','--vigenere_table', type = str, required = True, help='table that indicates the number of positions to shift the key')
    
    args = parser.parse_args()
    input = ''
    if args.text != '':
        input += args.text.lower()
    if args.filename != None:
        # TODO: implement read file
        input += ' ' + args.filename
    args.input = input
    if args.command == 'vigenere':
        args.shift = args.vigenere_table
    args.key = ALPHABETS[args.alphabet]

    return args