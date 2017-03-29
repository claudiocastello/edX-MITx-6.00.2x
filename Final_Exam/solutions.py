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


##########

#
# Probelem 6
#
import numpy as np
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
    import itertools
    binaryCombinations = [list(i) for i in itertools.product([0, 1], repeat=(len(choices)))]
    possibleResults = []
    for result in binaryCombinations:
        sumChoicesTimesResult = 0
        for i in range(len(choices)):
            sumChoicesTimesResult += choices[i] * result[i]
            if sumChoicesTimesResult > total:
                break
        if sumChoicesTimesResult <= total:
            possibleResults.append((result, sumChoicesTimesResult))
    orderedPossibleResults = sorted(possibleResults, key=lambda tup: tup[1], reverse = True)
    chosenResult = orderedPossibleResults[0]
    for j in range(len(orderedPossibleResults) - 1):
        if orderedPossibleResults[j+1][1] < orderedPossibleResults[j][1]:
            break
        else:
            sum2 = sum(orderedPossibleResults[j+1][0])
            if sum2 < sum(chosenResult[0]):
                chosenResult = orderedPossibleResults[j+1]
    return np.array(chosenResult[0])

import random
import pylab

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    probRabRepr = 1.0 - (CURRENTRABBITPOP / MAXRABBITPOP)

    reproductSuccess = random.random()

    if reproductSuccess < probRabRepr:
        CURRENTRABBITPOP += 1


def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    probFoxGiveBirth = 1/3

    probFoxDies = 1/10

    probFoxEatsRabbit = CURRENTRABBITPOP / MAXRABBITPOP

    for fox in range(CURRENTFOXPOP):
        huntSuccess = random.random()

        if huntSuccess < probFoxEatsRabbit and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            foxBirthSuccess = random.random()
            if foxBirthSuccess < probFoxGiveBirth:
                CURRENTFOXPOP += 1
        else:
            foxDieChance = random.random()
            if foxDieChance < probFoxDies and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1
    

def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    stepRabbitPop = 0
    stepFoxPop = 0
    popList = ([],[])
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        stepRabbitPop = CURRENTRABBITPOP
        stepFoxPop = CURRENTFOXPOP

        popList[0].append(stepRabbitPop)
        popList[1].append(stepFoxPop)

    pylab.figure('Rabbits and Foxes')
    pylab.clf()
    pylab.plot([step for step in range(numSteps)], popList[0], 'b-', label = 'Rabbit Pop')
    pylab.plot([step for step in range(numSteps)], popList[1], 'r-', label = 'Fox Pop')
    pylab.legend(loc = 'best')
    pylab.title('Foxes and Rabbits Population')
    pylab.xlabel('Step')
    pylab.ylabel('Population')

    return popList

# Test with Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

runSimulation(200)
