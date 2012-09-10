# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

def IsPrime(x):
   for i in range (2, math.ceil(math.sqrt(x))+1):
      if x%i == 0:
         return False
   return True
      
      
      
def Prime():
   i = 1
   while True:
      if IsPrime(i):
         yield i
      i += 1
      
num = 600851475143
      
j = 1
for i in Prime():
   if j == 10001:
      print (i)
      break
   j+=1
   
      