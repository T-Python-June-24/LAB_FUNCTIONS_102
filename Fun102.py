

def is_prime(num) -> bool:
    if num <= 1: # 0 and 1 are not primes
        return False
    if num == 2:
        return True
    if num % 2 == 0: # Even numbers
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
        
def find_primes(x:int, y:int):
    primes=""
    for i in range (x,y+1):
        if is_prime(i):
            primes += str(i)+"\n"

    print(f"\nPrimes between `{x}` and `{y}` are:")
    print(primes)

print("Welcome to Prime Checker!!")
x = int(input("Enter your start number: "))
y = int(input("Enter your end number:  "))
find_primes(x,y)
print("THANKS :)")
