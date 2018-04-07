# Roisin Anglim
# A program that displays Fibonacci numbers. 
# My name is Róisín, so the first and last letter of my name (R + N = 18 + 14) give the number  32. The 32nd Fibonacci number is 2,178,309.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
RN = 32
ans = fib(RN)
print("Fibonacci number", RN, "is", ans)
