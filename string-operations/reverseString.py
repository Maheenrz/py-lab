# Exercise 2
# Write a function printReverseString which takes a sentence under the string format as input (e.g. "Hello world!")
#  and prints the sentence with words in the reverse order (e.g. "world! Hello").
# Tips:
# • A sentence is an ensemble of words separated by spaces
# • The Python string methods split and join should be useful for this exercise
def printReverseString(sentence):
    sentence_split = sentence.split()
    sentence_split.reverse()
    reversed_str = " ".join(sentence_split)
    print(reversed_str)


printReverseString("Hello world!")    







# Exercise 3
# Write a function distanceToSun which asks the user to input the name of a planet of our solar system in command line,
#  and prints the distance between the planet and the Sun in kilometres.
# Tips:
# • Pick the online source of your choice to find distances between planets and the Sun.
# • Asking for a user input in terminal can be done using the userInput =
# input("text to display") syntax.
# • Remember to treat the case where the user input is invalid.
# • Stopping a function can be done using return
def distanceToSun():
    planet_distances = {
        "Mercury": 57900000,     # 57.9 million km
        "Venus": 108200000,      # 108.2 million km
        "Earth": 149600000,      # 149.6 million km
        "Mars": 228000000,       # 228 million km
        "Jupiter": 778000000,    # 778 million km
        "Saturn": 1430000000,    # 1.43 billion km
        "Uranus": 2870000000,    # 2.87 billion km
        "Neptune": 4500000000    # 4.5 billion km
    }

    planet = input("Enter the name of planet: ")
    while planet not in planet_distances:
        planet = input("Invalid! Enter a valid planet name: ")

    print(f"The distance between {planet} and the Sun is {planet_distances[planet]} km")


distanceToSun()



# Write a Python program that implements a function computeCost to compute the 
# Mean Squared Error (MSE) for univariate linear regression. The function should
# take the following parameters:
# • X: A list of m data points (a list of m real numbers).
# • y: A list of m target values (a list of m real numbers corresponding to X).
# • bias: The intercept parameter (a real number).
# • weight: The slope parameter (a real number).
# • The function should return the cost, computed using the MSE formula.
import numpy as np
def computeCost(X, y, w, b):
    # 1/2m summation (y' - y)^2
    m = len(X)
    y=np.array(y)
    X=np.array(X)
    # y'--> predicted value y' = b + w * X
    predictions = w * X + b
    errors = predictions - y
    mse = (1/(2 * m)) * np.sum(errors ** 2)
    return mse


X = [1,2,3,4,5,6]
y=[2,4,6,8,10,12]
b=0.0
w=2

print(computeCost(X,y,w,b))



    
    






# • Write a Python program that calculates the cost for different
#  combinations of parameters and prints the minimum cost
#  along with the optimal parameters. The program should include a function findMinCost that takes
#  the following parameters:
# • X: A list of m data points (a list of m real numbers).
# • Y: A list of m target values (a list of m real numbers corresponding to X).
# • bias_lst: A list of k possible values for the intercept parameter (a list of k real numbers).
# • weight_lst: A list of j possible values for the slope parameter (a list of j real numbers).
# • The function should compute the cost for each combination of intercept (from bias_lst) 
# and slope (from weight_lst), and return the minimum cost and the corresponding parameters.

