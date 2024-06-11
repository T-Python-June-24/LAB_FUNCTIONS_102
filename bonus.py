def string(text:str):
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