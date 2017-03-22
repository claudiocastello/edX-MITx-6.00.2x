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
You are given the following function and class and function specifications for the two coding problems on this page (also available in this file, die.py):
die.py

Write a function called makeHistogram(values, numBins, xLabel, yLabel, title=None), with the following specification:

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
    You should only be using the pylab.hist, pylab.title, pylab.xlabel, pylab.ylabel, pylab.show functions from the pylab module.
    Do not leave any debugging print statements when you paste your code in the box.
