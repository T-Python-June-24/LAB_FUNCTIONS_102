def find_primes(start:int, end:int):
    '''
    Takes two positive integers and prints all prime numbers between them

    Args:
        start (int): The beginning of the sequence.
        end (int): The end of the sequence.
    
    Returns:
        None: Prints the prime numbers found between start and end.
    '''
    # Check if the integers are positive and skip the integer 1,
    # since it's known that 1 is not a prime number.
    if start > 1 and end > 1:
        if start < end:
            # Check whether the current integer is a prime or not.
            for prime_candidate in range(start, end + 1):
                # To count how many divisors the current integer has.
                # A prime number has only 2 divisors.
                divisors = 0
                for divisor in range(1, prime_candidate + 1):
                    if prime_candidate % divisor == 0:
                        divisors += 1
                    # Since the loop was terminated using break, the integer is not prime.
                    if divisors > 2:
                        break
                # Since the loop was terminated normally the integer is prime.
                else:
                    print(prime_candidate)
        else:
            print("The last integer must be greater than the first!")
    else:
        print("Integers must be positive!")

x:str  = input("Enter the first positive integer: ")
y:str = input("Enter the last positive integer: ")
if x.isdigit and y.isdigit:
    find_primes(int(x), int(y))
else:
    print("You must enter an integer...")