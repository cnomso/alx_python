#Write a function that returns a tuple with the length of a string and its first character.

def multiple_returns(sentence):
    length = len(sentence)
    first_character = sentence[0] if length > 0 else None
    return length, first_character