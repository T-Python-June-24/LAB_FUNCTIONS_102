def find_primes( num1:int , num2:int)->None:
    primeNumbers=[]
    
    for i in range(num1+1,num2):
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
        if is_prime:
            primeNumbers.append(i)
    for primes in primeNumbers:
        print(primes)

num1=int(input("please enter first number: "))
num2=int(input("please enter second number: "))

find_primes(num1,num2)
        