def find_primes(num1:int, num2:int):
    '''A function in which only odd numbers are displayed
    Args:
        num1 (int): First issue
        num2 (int): The second issue
    
    '''
    for i in range(num1 , num2 ):
        if i % 2 ==1:
            print(i)
        
    
find_primes(25 , 50)