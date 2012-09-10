# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def IsPrime(x):
   for i in range (2, math.ceil(math.sqrt(x))+1):
      if x%i == 0:
         return False
   return True
      
      
      
def Prime(max):
   i = 1
   while i<max:
      if IsPrime(i):
         yield i
      i += 1
      
num = 600851475143
      
for i in Prime(math.sqrt(num)):
   if num % i == 0:
      num /= i
   if num == 1:
      print(i)
      break
      
      
      
      
   
      
      
      