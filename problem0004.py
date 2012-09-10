# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def IsPalin(x):
   s = str(x)
   if s == s[::-1]:
      return True
   return False
   
   

min = 99
max = 999

n = 0

for i in range(max, min, -1):
   for j in range(max, min, -1):
      if IsPalin(i*j):
         if i*j>n:
            n = i*j

print (n)         

         
