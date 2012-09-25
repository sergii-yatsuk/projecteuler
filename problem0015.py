#Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.
#How many routes are there through a 2020 grid?
import math

n = 20
k = math.factorial(2*n)/math.pow(math.factorial(n), 2)
print (k)

