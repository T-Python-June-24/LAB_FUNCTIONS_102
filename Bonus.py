

def separate_word(user_word:str):
 '''
 this function takes a string from user and then separate it in camel case 
 Args
 user_word(string): input text from user 
 '''
 new_word:str= ""
 for i in user_word: #iterate each letter in word 
    if i.isupper():# check if the leter is upper and retrun true 
        new_word +=  " "+ i.lower() # space after each Upper letter and convert the upper into lower 
    else:
        new_word += i # if letter is alreday a lower 
 return new_word 

user_word:str= input("Enter your word: ") 
while True:
 if  user_word.isalpha(): # check if the type is string 
  new_word=separate_word(user_word) 
  print(new_word)
  print(separate_word.__doc__)
  break
 else:#type is not a string 
   user_word= input("Envalid value ,Enter a string word: ") 
 