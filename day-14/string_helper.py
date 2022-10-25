import math


def change_case(orig_string: str):
    for i in orig_string:
        if i.islower():
            orig_string = orig_string.replace(i, i.upper())
        elif i.isupper():
            orig_string = orig_string.replace(i, i.lower())
    return orig_string


def split_in_half(orig_string: str):
    half_strings = ()
    half_length = math.floor(len(orig_string) / 2)
    split_string1 = orig_string[:half_length]
    split_string2 = orig_string[half_length:]
    half_strings = (split_string1, split_string2)
    return half_strings


def remove_special_characters(orig_string: str):
    for i in orig_string:
        if (
            i.islower() == False
            and i.isupper() == False
            and i.isnumeric() == False
            and i.isspace() == False
        ):
            orig_string = orig_string.replace(i, "")
    return orig_string
