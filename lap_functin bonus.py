def string_seperator(string:str) -> str:
    '''
    Takes a string and seperates
    capital letter and replaces
    with a lower letter
    '''
    if type(string) == str:
        string2 = ""
        for character in string:
            if character.isupper():
                string2 += f" {character.lower()}"
            else:
                string2 += character
    return string2

print(string_seperator(input("Enter a string: ")))
help(string_seperator.__doc__)