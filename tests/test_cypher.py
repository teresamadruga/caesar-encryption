"""Test funtions of cypher.py"""

import pytest

from src.cypher import caesar_cypher, encrypt, vigenere_cypher
from src.parse import ALPHABETS


def test_on_caesar_alphabets():
    """Test caesar code result"""
    assert (
        encrypt(caesar_cypher, "ezevkvveky tveklip", 9, ALPHABETS["en"])
        == "nineteenth century"
    )


def test_on_caesar_non_alphabets():
    """Test caesar code result"""
    assert (
        encrypt(caesar_cypher, "&*48(£^ )+ =_39-", 15, ALPHABETS["es"])
        == "&*48(£^ )+ =_39-"
    )


def test_on_vigenere_alphabets():
    """Test vigenere code result"""
    assert (
        encrypt(vigenere_cypher, "attackatdawn", "lemon", ALPHABETS["en"])
        == "lxfopvefrnhr"
    )


def test_on_vigenere_non_alphabets():
    """Test vigenere code result"""
    assert (
        encrypt(vigenere_cypher, "attackatdawn", "l3m0n", ALPHABETS["en"])
        == "ltfapvafdnhn"
    )
