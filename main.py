def find_primes(num1, num2):
    """
    Finds all prime numbers between two given numbers

    Args:
        num1 (int): The first number
        num2 (int): The second number
        
    Returns:
        str: A string containing all the prime numbers between num1 and num2
    """
    primes = ""
    for num in range(num1, num2 + 1): # +1 because we want it to be inclusive
        if num > 1:  # prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes += str(num) + ", "
    return primes[:-2] # remove the last comma and space

# --------------------------------------------------

def small_letters_converter(sentence: str) -> str:
    """
    Converts all the letters in a sentence to lowercase

    Args:
        sentence (str): The sentence to be converted

    Returns:
        str: The sentence in lowercase
    """
    if isinstance(sentence, str):   
        for letter in sentence:
            if letter.isupper():
                sentence = sentence.replace(letter, " " + letter.lower())
    return sentence


# test cases
input_for_find_primes_num1 = int(input("Enter the first number: "))
input_for_find_primes_num2 = int(input("Enter the second number: "))
print(find_primes(input_for_find_primes_num1, input_for_find_primes_num2))

input_for_small_letters_converter = input("Enter a sentence: ")
print("The converted sentence is: " + small_letters_converter(input_for_small_letters_converter))



