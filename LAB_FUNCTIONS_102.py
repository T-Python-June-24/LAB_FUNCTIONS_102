
def find_primes(first_number: int, second_number: int):
    '''
    this function prints the prime numbers in range given by the user from the first_number to second_number (inclusive).
    Args :
    first_number(int) : define the beginig of a range
    first_number(int) : define the end  of a range 
    '''
    for i in range(first_number, second_number + 1): 
            for j in range(2, int(i ** 0.5) + 1): # the range of possible factors for the current number
                if i % j == 0:
                    break
            else :
                print(i)
first_number=int(input("Enter the first number : "))
second_number=int(input("Enter the second number : "))
find_primes(first_number, second_number)
print(find_primes.__doc__)