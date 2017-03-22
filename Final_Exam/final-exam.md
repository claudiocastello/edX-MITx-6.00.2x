# Final Exam

## Problem 3-2
Write a Monte Carlo simulation to solve the above problem. Feel free to write a helper function if you wish.

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 

Paste your entire function (including the definition) in the box.

Restrictions:

    Do not import or use functions or methods from pylab, numpy, or matplotlib.
    Do not leave any debugging print statements when you paste your code in the box.

## Problem 4-1
You are given the following function and class and function specifications for
the two coding problems on this page (also available in this file, die.py):
[die.py](https://github.com/claudiocastello/edX-MITx-6.00.2x/blob/master/Final_Exam/die.py)

Write a function called makeHistogram(values, numBins, xLabel, yLabel, title=None),
with the following specification:

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """

Paste your entire function (including the definition) in the box.

Restrictions:

    Do not paste import pylab in the box.
    You should only be using the pylab.hist, pylab.title, pylab.xlabel,
    pylab.ylabel, pylab.show functions from the pylab module.
    Do not leave any debugging print statements when you paste your code in the box.
    
## Problem 4-2
Write a function called getAverage(die, numRolls, numTrials), with the following specification:

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """

A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:

    a dice roll of 1 4 3 has a longest run of 1
    a dice roll of 1 3 3 2 has a longest run of 2
    a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3

When this function is called with the test case given in the file, it will return 5.312.
Your simulation may give slightly different values.

Paste your entire function (including the definition) in the box.

Restrictions:

    Do not import or use functions or methods from pylab, numpy, or matplotlib.
    Do not leave any debugging print statements when you paste your code in the box.

If you do not see the return value being printed when testing your function, close the histogram window.
Code Editor

## Problem 6
Write a function that meets the specifications below. You do not have to use dynamic programming.

Hint: You might want to use bin() on an int to get a string, get rid of the first two characters,
add leading 0's as needed, and then convert it to a numpy array of ints. Type help(bin) in the console.

For example,

    If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
    If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
    If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]

More specifically, write a function that meets the specifications below:

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """

Paste your entire function (including the definition) in the box. Note: If you want
to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code.
Unfortunately, pylab does not work with the grader.


## Problem 8
For this problem you are going to simulate growth of fox and rabbit population in a forest!

The following facts are true about the fox and rabbit population:

    The maximum population of rabbits is determined by the amount of vegetation in the forest,
    which is relatively stable.

    There are never fewer than 10 rabbits; the maximum population of rabbits is 1000.

    For each rabbit during each time step, a new rabbit will be born with a probability of
    prabbit reproduction
    
    (P rabbit reproduction) = 1.0 − (current rabbit populationmax / rabbit population)

    In other words, when the current population is near the maximum, the probability
    of giving birth is very low, and when the current population is small, the probability
    of giving birth is very high.

    The population of foxes is constrained by number of rabbits.

    There are never fewer than 10 foxes.

    At each time step, after the rabbits have finished reproducing, a fox will try
    to hunt a rabbit with success rate of (P fox eats rabbit)
    
    (P fox eats rabbit) = current rabbit population / max rabbit population

    In other words, the more rabbits, the more likely a fox will eat one.

    If a fox succeeds in hunting, it will decrease the number of rabbits by 1 immediately.
    Remember that the population of rabbits is never lower than 10.

    Additionally, if a fox succeeds in hunting, then it has a 1/3 probability of giving
    birth in the current time-step.

    If a fox fails in hunting then it has a 10 percent chance of dying in the current time-step.
    If the starting population is below 10 then you should do nothing. You should not increase
    the population nor set the population to 10.

Start with 500 rabbits and 30 foxes.

At the end of each time step, record the number of foxes and rabbits.

Run the simulation for 200 time steps, and then plot the population of rabbits and the population of foxes as a function of time step. (You do not need to paste your code for plotting for Part A of this problem).

Use the following steps, and the template file [rabbits.py](https://github.com/claudiocastello/edX-MITx-6.00.2x/blob/master/Final_Exam/rabbits.py), as guides in your implementation of this simulation.

Step 1: Write the procedure, rabbitGrowth, that updates the number of rabbits during the first part of a time step

Step 2: Write the procedure, foxGrowth, that updates the number of rabbits and foxes during the second part of a time step

Step 3: Write the master procedure, runSimulation, that loops for some amount of time steps, doing the first part and then the second part of the simulation. Record the two populations in two different lists, and return those lists.

Paste your code for the three functions rabbitGrowth, foxGrowth, and runSimulation in the following box.
WARNING

CLARIFICATIONS / HINTS

    "See Full Output": If you are getting the line "0 10" in your output for "Test 4 foxGrowth"
    then for this particular test, your code changes the CURRENTFOXPOP (increases it if the fox
    population has gone below the minimum fox population), which is not the right behavior -- the
    code should not reset CURRENTFOXPOP.
    It is not correct to assume that there is a 1/3 chance that the population increases in "Test 3
    foxGrowth". Pay special attention to the following statement in the docstring of foxGrowth():
    Each fox, based on the probabilities in the problem statement, may eat one rabbit (but only if
    there are more than 10 rabbits).
