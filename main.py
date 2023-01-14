from parse import args_parse
from cypher import caesar_cypher, vigenere_cypher, encrypt


args = args_parse()
# print(encrypt(caesar_cypher, args.input, args.shift, args.key))
print(encrypt(vigenere_cypher, args.input, 'lemon', args.key))