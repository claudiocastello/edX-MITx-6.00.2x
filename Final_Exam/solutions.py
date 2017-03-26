#
# Problem 3-1 / Monte Carlo Simulation
#

import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    counter = 0
    for trial in range(numTrials):
        bucket = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        sample = random.sample(bucket, 4)
        if sample[0] == sample[1] and sample[1] == sample[2]:
            counter += 1
    return round(float(counter/numTrials),3)

######

#
# Problem 4
#
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins, normed=False, range=(0,numBins))
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)

# x = []
# for i in range(500):
#     x.append(random.randint(0,100))

# makeHistogram(x, 20, 'Values', 'Frequency')

### Helper ###
#
def longestRun(inputList):
    longestRun = 1
    counter = 1
    for i in range(len(inputList) - 1):
        if inputList[i + 1] == inputList[i]:
            counter += 1
        else:
            if counter > longestRun:
                longestRun = counter
            counter = 1
    return longestRun
#
### End Helper ###
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longestRunList = []
    for trial in range(numTrials):
        diceRoll = []
        for roll in range(numRolls):
            diceRoll.append(die.roll())
        longestRunList.append(longestRun(diceRoll))
    mean, std = getMeanAndStd(longestRunList)
    makeHistogram(longestRunList, 10, 'Longest Run', 'Frequency', 'The Dice!')
    return round(mean, 3)

# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
