def find_primes(num1:int, num2:int):
    
    for num in range(num1, num2 + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

find_primes(25, 50)
