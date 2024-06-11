def lowerTheUpper(word:str):
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
