def string(s:str):
    if isinstance(s, str) == True:
        splitting=""
        for i in s:
            if(i.isupper()):
                splitting+=" "+i
            else:
                splitting+=i
        listed=splitting.split(" ")

        print(' '.join([str(item) for item in listed]))
    else:
        print("That wasn't a string")

string(s=str(input("insert a connected sentence in Camel way: ")))