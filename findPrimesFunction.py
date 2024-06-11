def find_primes(start:int, end:int):
    """"
    It prints all prime numbers between any two given integer numbers.
    Args:
        start (int): The start number
        end (int): The end number
        
    Return:
        None
    """
    for number in range(start, end+1):
        count = 0
        for i in range(2,number):
            if number % i == 0:
                count += 1
        if count == 0:
            print(number)


find_primes(25,50)