# Write a program printNegative which prints all negative elements 
# of an integer or float input list.

def printNegative(inputList):
    for element in inputList:
        if element < 0:
            print(element)


printNegative([-2,3,4,6,0.9,-9,99,44,-0.4])            