# Write a program filterOdd which takes a list of integers as input
# and returns a sub-list of the input containing only its odd elements
#  (tip: the Python modulo operator is %; e.g. 7%2 returns 1).


def filterOdd(inputList):
   sub_list = [val for val in inputList if val%2!=0]
   return sub_list


sub_list = filterOdd([2,1,7,8,33,24,15,28,44,55])    
print(sub_list)