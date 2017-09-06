def problem_1():

  #This is the solution to the first Project Euler problem from
  #https://projecteuler.net/problem=1:

  #If we list all the natural numbers
  #below 10 that are multiples of 3 or 5,
  #we get 3, 5, 6 and 9. The sum of these
  #multiples is 23.
  #Find the sum of all the multiples of 3
  #or 5 below 1000.

  #Solution:
  #1. for each i under 1000 check if multiple of 3 or 5
  #2. save i to array'
  #3. add up elements of the array

  i=1
  n=0

  for i in range (1,1000):
      if ((i % 3 == 0) or (i % 5 == 0)):
            n = n + i
            next
  print n


problem_1()
