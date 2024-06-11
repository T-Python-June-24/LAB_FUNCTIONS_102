def find_primes(first_num:int , secon_num:int ):
    '''
    the function takes in 2 parameters of type int , and print the prime numbers 
    between the first parameter and the second parameter .
    
    '''
    if first_num < 2 : 
        first_num = 2 

    for i in range(first_num,secon_num+1):
        if i > 1 :
            for j in range(2,int(i**0.5)+1):
                if i % j == 0 :
                    break
            else:
                print(i)

find_primes(25,50)