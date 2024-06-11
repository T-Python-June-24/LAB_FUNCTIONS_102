def lowerTheUpper(word:str):
    """"
    It takes a string as a parameter then checks if it's indeed of string type.
    It separates the string at any capital letter and replace it with a small letter 
    then return the new word.
    Args:
        word (str): The string to be separated
        
    Return:
        newWord: a new string where all upper letters are replace with lower ones.
    """
    newWord = ""
    if word.isalpha():
        for i in word:
            if i == i.upper():
                newWord += " " + i.lower()
            else:
                newWord += i
    return newWord

str = lowerTheUpper("helloWorldThere")
print(str)
