# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def IsMult35(x):
   if x%3 == 0 or x%5 == 0:
      return True
   return False


sum = 0
for i in range (1, 1000):
   if IsMult35(i):
      sum += i 
print (sum)
   