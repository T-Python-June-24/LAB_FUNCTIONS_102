def separater(a) -> str:
    if not a.isalpha():
        print("Sorry, you have to enter string only.")
        exit()

    new_a = ""
    for char in a:
        if char.isupper():
            new_a +=" "+char.lower()
        else:
            new_a+= char
    return new_a

A = input("Enter string to separate it: ")
print("The new modified string is: (" + separater(A) + ")")
