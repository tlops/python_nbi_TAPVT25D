#!/usr/bin/python3
## test if a word or sentence is palindrome. 

import pytest
from palindrome import is_palindrome
     
@pytest.mark.parametrize("word, expected_result", [
    # Test case for a simple palindrome.
    ("level", True),
    # Test case for a non-palindrome.cat 
    ("python", False),
    # Test case for a case-insensitive palindrome.
    ("Racecar", True),
    # Another test case for a different palindrome.
    ("A man a plan a canal panama", True),
    # Test case for a palindrome with spaces and punctuation.
    ("No 'x' in 'Nixon'!", True),
    # Test case for an empty string.
    ("", True),
    # Test case for a single-character string.
    ("a", True)
    ])


def test_is_palindrome(word, expected_result):
    # Tests if a given word is a palindrome using multiple test cases.
    assert is_palindrome(word) == expected_result


