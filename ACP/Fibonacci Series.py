def recursive_fib(n):
   if n <= 1:
       return n
   else:
       return(recursive_fib(n-1) + recursive_fib(n-2))

nterms = int(input("Enter Number of Terms :"))

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recursive_fib(i))
