def string_seperator(string:str) -> str:
    '''
    Takes a string and seperates
    the word at any capital letter and replaces
    it with a lower letter

    Args:
        string (str): A sequence of characters.

    Returns:
        new_string (str): Modified string with capital letters replaced with lower letters.
    '''
    # First check that the type of the parameter is of type str
    if type(string) == str:
        new_string = ""
        for character in string:
            # Seperate the word at any capital letter and
            # replaces it with a lower letter
            if character.isupper():
                new_string += f" {character.lower()}"
            else:
                new_string += character
    return new_string

print(string_seperator(input("Enter a string: ")))