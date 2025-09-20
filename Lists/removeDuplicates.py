# Write a program removeDuplicate which takes a list of any 
# type as input, and returns a list without any duplicate elements as output.

def removeDuplicates(inputList):
    no_duplicates = list(dict.fromkeys(inputList))
    print(no_duplicates)



removeDuplicates([2,3,4,5,3,2,1,5,6,7,8,9,1,0,4,3,2])    

