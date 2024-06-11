
def toRegularStyle(string:str)->str:
    
    modified_string = ""

    for i in string:
                
        if i.isupper():
                    
            modified_string += " "+i.lower() 
                    
        else:
                    
            modified_string += i 

    return modified_string

user_input = "plase enter a sentance ! "

while not user_input.isalpha():
        
    user_input = input("plase enter a sentance !  ")


new_word = toRegularStyle(user_input)

print(new_word)
