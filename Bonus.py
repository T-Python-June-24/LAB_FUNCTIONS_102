def stringModifier (name:str) -> str:
    ''' This function is to Convert Upper letter to lower and separate between the word

        Args:
        name (str): Any word

        Returns: 
        str: Modify string 
    '''
    if not  isinstance(name,str):
        print("Wrong!, Enter String Value")
    ModifyStr =""
    for word in name:
        if word.isupper():
            ModifyStr += " " + word.lower()
        else: 
            ModifyStr += word
    return ModifyStr

print(stringModifier("HelloWorldThere"))
print(stringModifier("Abdulaziz Asiri"))
    