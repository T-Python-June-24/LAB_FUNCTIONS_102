def find_primes(primes1:str , primse2:str):
   for n in range(primes1, primse2 +1 ):
        if n > 1:  # primes are greater than 1
            for i in range(2, n):
                if (n % i) == 0:  
                    break
            else:
                print(n)

find_primes(primes1=20,primse2=60)


'''
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