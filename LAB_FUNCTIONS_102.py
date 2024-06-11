'''
# LAB_FUNCTIONS_102

## Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter . 

### hint
a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers


#### for example, primes between `25` and `50` are:
```
29   
31   
37   
41   
43   
47   
'''


def findPrime(start:int, end:int):
    for number in range(start, end + 1):
        if number > 1:  # primes are greater than 1
            for i in range(2, number):
                if (number % i) == 0:  
                    break
            else:
                print(number)
                               
findPrime(start=25,end=50)





'''

# Bonus
## write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: `helloWorldThere` should return :
```hello world there```


'''


def split_word_and_lowercase(string: str) -> str:
    if not isinstance(string, str):
        return "Oops, something went wrong. It looks like you did not enter a string value, sir."
    
    array = []
    for char in string:
        if char.isupper() and array:
            array.append(' ')
            array.append(char.lower())
        else:
            array.append(char)
    
    return ''.join(array)

print(split_word_and_lowercase("helloWorldThere")) 
        
