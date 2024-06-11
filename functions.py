
def find_primes(p:int, q:int):

    for num in range(p, q + 1):
        if num > 1:
            is_prime = True  #local variable
            i = 2
            while i * i <= num:
                if num % i == 0:
                    is_prime = False
                i += 1
            if is_prime:
                print(num)


find_primes(25, 50)
