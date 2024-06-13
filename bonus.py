def string(text:str):
    '''A function that edits text, converts uppercase letters to lowercase, and places a space before the letter
    Args:
        (string): The text to be modified
    return:
    text1 (str): Text after modification
    '''
    text1:str= ""
    if type(text)== str:
        for i in text:
            if i.isupper()== True:
                i=" "+i.lower() 
            text1 = text1 + i
        return text1 
    else:
        return "The entered value is not text"
print(string("helloWorldThere"))