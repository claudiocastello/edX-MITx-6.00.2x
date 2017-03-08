###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    # Create an empty list that will be returned with sublists represeting the various trips with allocated cows
    mainList = []

    # Create an empty set to store cows already checked
    storeSet = set([])

    # Create a sorted list of tuples of the cowsCopy dictionary to avoid mutations in this data
    sortedCows = sorted(cows.items(), key=lambda x: x[1], reverse = True)

    # This while loop will do the following:
    #   1. Create an empty list to temporary store the selected cows for the ship
    #   2. Create a totalWeight variable setted to 0, to help decide if a cow goes or not in the ship
    while len(sortedCows) != len(storeSet):
        tempList = [] # Create a sublist to be appended in the main list
        totalWeight = 0

        for cow in range(len(sortedCows)):
            if (sortedCows[cow][0] not in storeSet):
                if (sortedCows[cow][1] > limit):
                    storeSet.add(sortedCows[cow][0])
                else:
                    if (totalWeight + sortedCows[cow][1] <= limit):
                        tempList.append(sortedCows[cow][0])
                        totalWeight += sortedCows[cow][1]
                        storeSet.add(sortedCows[cow][0])

        # After looking each cow available, tempList is appended to mainList and the loop starts again
        mainList.append(tempList)

    return mainList


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    # Create a partitioned list of cows dictionary keys (see get_partitions() documentation for more details)
    # Each sublist of cowsPartition contain sublists that represents possible allocation of cows in spaceships
    # e.g. If cows are {'a':2, 'b':3, 'c':4}, cowsPartition will be [[['a', 'b', 'c']], [['a', 'b'], [c]], [['a', 'c'], ['b']], [['c', 'b'], ['a']], [['a'], ['b'], [c]]]
    # Each of these partitions are possible allocations for cows in spaceship and need to be tested with brute force algorithm to get the best one
    from copy import copy

    cowsCopy = cows.copy()

    for cow in cows.keys():
        if cows[cow] > limit:
            del cowsCopy[cow]

    cowsPartition = list(get_partitions(cowsCopy.keys()))

    bestSublist = []

    savedList = []

    # The spaceship total weigth need to be less or equal to limit and if any trip in the partition is above limit this partition could be disconsidered
    for sublist in cowsPartition:

        for partition in sublist:
            partitionWeight = 0

            for cow in partition:
                partitionWeight += cows[cow]

            if partitionWeight > limit:
                bestSublist = savedList
                break

            else:
                if len(bestSublist) == 0 or len(sublist) <= len(bestSublist):
                    bestSublist = sublist[:]

        savedList = bestSublist

    return bestSublist


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
