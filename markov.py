from random import choice
from sys import argv

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_path = argv[1]
    text = open(file_path).read()

    return text


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    split_text = text_string.split()
    for i in range(len(split_text)-2):
        current_key = (split_text[i], split_text[i+1])
        third_word = split_text[i+2]
        if current_key in chains:
            chains[current_key].append(third_word)
        else:
            chains[current_key] = [third_word]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    print chains
    # start = ()
    start = choice(chains.keys())
    while start in chains:
        third = choice(chains[start])
        text = text + ' ' + third
        start = (start[1], third)
    # text = text + ' ' + start[1]    
    return text


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
