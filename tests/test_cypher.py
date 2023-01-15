"""Test funtions of cypher.py"""

import pytest

from src.cypher import caesar_cypher, encrypt, vigenere_cypher
from src.parse import ALPHABETS


def test_on_caesar():
    """Test caesar code result"""
    assert (
        encrypt(caesar_cypher, "ezevkvveky tveklip", 9, ALPHABETS["en"])
        == "nineteenth century"
    )


def test_on_vigenere():
    """Test vigenere code result"""
    assert (
        encrypt(vigenere_cypher, "attackatdawn", "lemon", ALPHABETS["en"])
        == "lxfopvefrnhr"
    )
