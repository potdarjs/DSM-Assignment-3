# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 20:47:45 2018

@author: HP
"""

# Assignment 3 - Data Science Masters
# 1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

# MY Reduce function to work like python's built in reduce()
def myreduce(func, seq):

 # Get first item in sequence and assign to result
  result = seq[0]
 # iterate over remaining items in sequence and apply reduction function 
  for item in seq[1:]:
   result = func(result, item)

  return result
  
  # testing of myreduce function
def sum(a,b): return a + b
print ("Sum on list [4,5,6] using custom reduce function "   + str(myreduce(sum, [4,5,6])) )

# 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()
# myfilter function to work like python's buit in filter()
def myfilter(func, seq):

 # Initialize empty list
 result = []
 # iterate over sequence of items in sequence and apply filter function
 for item in seq:
  if func(item):
   result.append(item)

 # return funal output
 return result
 
 # testing myfilter function
def ispositive(x):
 if (x <= 0): 
  return False 
 else: 
  return True
  
  print ("Positive Integers from the list [0,1,-2,3,4,5] using myfilter function :"  
       + str(myfilter(ispositive, [0,1,-2,3,4,5])))
       
 # # 2. Implement List comprehensions to produce the following lists.
 
 word = "ACADGILD"
list = [ alphabet for alphabet in word ]
print ("List of Alphabets in word 'ACADGILD' : \n" + str(list))

input_list = ['x','y','z']
input_range = range(1,5)
result = [ item*num 
          for item in input_list 
          for num in input_range  ]
print("From ['x','y','z'] : \n" +   str(result))

input_list = ['x','y','z']
result = [ item*num 
          for num in range(1,5) 
          for item in input_list  ]
print("From ['x','y','z']:\n" +   str(result))

input_list = [2,3,4]
result = [ [item+num] 
          for item in input_list 
          for num in range(0,3)]
print("From [2,3,4] :\n" +  str(result))

input_list = [2,3,4,5]
result = [ [item+num for item in input_list] 
          for num in range(0,4)  ]
print("From [2,3,4,5]:\n" +  str(result))

input_list=[1,2,3]
result = [ (a,b) for b in input_list 
          for a in input_list]
print("From [1,2,3]:\n" +  str(result))


# 3. Implement a function longestWord() that takes a list of words and returns the longest one

from functools import reduce
list_words = ["Indian", "Economy", "is", "Growing"]

# Function to return longest word in the given list
def longestWord(list_words):
 return reduce( (lambda x,y:
                 y if len(y) > len(x) 
                 else x),
               list_words )

print ('Longest word in ["Indian", "Economy", "is", "Growing"] is ' + longestWord(list_words) )