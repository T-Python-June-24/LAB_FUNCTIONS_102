def find_primes(num1: int, num2: int):
    '''A function to display prime numbers between two given numbers.
    Args:
        num1 (int): First number.
        num2 (int): Second number.
    '''
    for i in range(num1, num2 + 1):
        if i > 1:  
            is_prime = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print(i)


find_primes(25, 50)
