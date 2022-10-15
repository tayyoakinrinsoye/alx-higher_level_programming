#!/usr/bin/python3
'''Function that prints a text with 2 new lines after
    characters(.,? and :
'''

def text_indentation(text):
    """Print text with two new lines after each '.', '?' , and ':'.

    Args:
        text(str): The text to print

    Raises:
        TypeError: if text is not a string.
    """

    if type(text) != str:
        raise TypeError("test must be a string")

    cursor = 0

    while cursor < len(text) and text[cursor] == ' ':
        cursor += 1

    while cursor < len(text):
        print(text[cursor], end="")
        if text[cursor] == "\n" or text[cursor] in ".,?:":
            if text[cursor] in ",.?:":
                print("\n")
            cursor += 1
            while cursor < len(text) and text[cursor] == ' ':
                cursor += 1
            continue
        cursor += 1
