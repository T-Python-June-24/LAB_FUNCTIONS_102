def smallLetter(word:str)->str:
    wordlist=[]
    returendWord=''
    if isinstance(word,str) :
        for i in word:
            if i.isupper():
                wordlist.append("")
                wordlist.append(i.lower())
            else:
                wordlist.append(i)
        for j in wordlist:
            if j=="":
                returendWord+=" "
            returendWord+=j
        return returendWord

print(smallLetter(str(input("Enter your word: "))))
