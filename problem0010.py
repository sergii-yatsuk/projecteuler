# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


import math

def IsPrime(x):
   if x == 2 :
      return True

   for i in range (2, math.ceil(math.sqrt(x))+1):
      if x%i == 0:
         return False
   return True
      
      
      
def Prime(max):
   i = 2
   while i<max:
      if IsPrime(i):
         yield i
      i += 1
      
sum=0
      
for i in Prime(2000000):
   sum += i
   
print (sum)