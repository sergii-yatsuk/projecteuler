# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isDiv(x):
   for i in range(1,21):
      if x%i !=0:
         return False
   return True


x = 20

while True:
   if isDiv(x):
      print(x)
      break
   x = x+20