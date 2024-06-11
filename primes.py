def findPrimes(x,y): 
    for n in range(x,y,1):
        if n > 1:
            for i in range(2, (n//2)+1):
                if (n % i) == 0:
                    break
            else:
                print(n)

print("This is an Application that provides the prime numbers between any 2 given numbers")
findPrimes(x = int(input("insert a positive integer greater than 2: ")),y = int(input("insert a positive integer greater than the previous one: ")))
