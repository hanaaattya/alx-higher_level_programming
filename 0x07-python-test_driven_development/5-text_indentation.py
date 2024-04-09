#!/usr/bin/python3
"""text_indintation"""
def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?' and ':' characters.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    modified_txt = ""

    for char in text:
        modified_txt += char

        if char in ['.', '?', ':']:
            modified_txt += '\n\n'

    print(modified_txt.strip())
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
