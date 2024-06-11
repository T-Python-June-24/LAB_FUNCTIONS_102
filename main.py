# definig the function

def find_primes(x:int, y:int) -> int:
  """
    this prints the prime number from the range of the giving parameters

    Args:
        x (int): this is the first input number and the start of the range
        y (int): this is the second input number and the end of the range

    Returns:
        int: prime numbers between x and y
  """
  print("Prime numbers between", x, "and", y, "are:")
  # looping through numbers in range
  for num in range(x, y + 1):
      # checking if the number is greater than 1
      if num > 1:
          # if greater than 1, start another loop to check if dividable from 2 up to the number
          for i in range(2, num):
              # If any divisor is found, break the loop. else, print the prime number.
              if (num % i) == 0:
                  break
          else:
              print(num)

find_primes(25, 50)