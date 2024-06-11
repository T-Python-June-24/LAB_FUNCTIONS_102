def find_primes(start:int, end:int):
    for number in range(start, end+1):
        count = 0
        for i in range(2,number):
            if number % i == 0:
                count += 1
        if count == 0:
            print(number)


find_primes(25,50)