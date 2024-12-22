#!/usr/bin/python3

# import std
import os
from string import ascii_lowercase
# import non-std

# import local

# globals/consts
target_file = 'books/frankenstein.txt'

# main

def main() -> None:
    with open(target_file) as file_obj:
        file_contents: str = file_obj.read()
    
    print(f"--- Begin report of {target_file} ---")
    print(f"{count_words(file_contents)} found in the document\n")

    for letter in ascii_lowercase:
        print(f"the '{letter}' character was found {count_char(file_contents,letter)} times")
# code blocks

def count_words(words: str) -> int:
    words_list: list[str] = words.split()
    return len(words_list)

def count_char(words: str, char: str) -> int:
    return words.lower().count(char.lower())

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    main()
