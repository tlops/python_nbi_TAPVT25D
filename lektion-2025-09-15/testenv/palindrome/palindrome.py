#!/usr/bin/python3i 

import re

def is_palindrome(word):
    # Checks if a given word is a palindrome.
    # returns True or False based on input

    # This addresses the case-insensitive requirement.
    processed_word = str(word).lower()

    # Remove all non-alphanumeric characters (like spaces, punctuation, etc.).
    # The 're.sub' function is used for this.
    processed_word = re.sub(r'[^a-z0-9]', '', processed_word)
    
    # This [::-1] reveres the processed_word
    reversed_word = processed_word[::-1]

    if processed_word == reversed_word:
        return True
    else: 
        return False


#print(is_palindrome("level"))
#print(is_palindrome("python"))
#print(is_palindrome("race car"))
