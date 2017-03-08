# Problem 1
#
# One way of transporting cows is to always pick the heaviest cow that will fit onto
# the spaceship first. This is an example of a greedy algorithm. So if there are
# only 2 tons of free space on your spaceship, with one cow that's 3 tons and another
# that's 1 ton, the 1 ton cow will get put onto the spaceship.
#
# Implement a greedy algorithm for transporting the cows back across space in the
# function greedy_cow_transport. The function returns a list of lists, where each
# inner list represents a trip and contains the names of cows taken on that trip.
#
# Note: Make sure not to mutate the dictionary of cows that is passed in!
#
# Assumptions:
#
#    The order of the list of trips does not matter. That is, [[1,2],[3,4]]
#    and [[3,4],[1,2]] are considered equivalent lists of trips.
#    All the cows are between 0 and 100 tons in weight.
#    All the cows have unique names.
#    If multiple cows weigh the same amount, break ties arbitrarily.
#    The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.
#
# Example:
#
# Suppose the spaceship has a weight limit of 10 tons and the set of cows
# to transport is {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.
#
# The greedy algorithm will first pick Jesse as the heaviest cow for the
# first trip. There is still space for 4 tons on the trip. Since Maggie
# will not fit on this trip, the greedy algorithm picks Maybel, the heaviest
# cow that will still fit. Now there is only 1 ton of space left, and none of
# the cows can fit in that space, so the first trip is [Jesse, Maybel].
#
# For the second trip, the greedy algorithm first picks Maggie as the heaviest
# remaining cow, and then picks Callie as the last cow. Since they will both fit,
# this makes the second trip [[Maggie], [Callie]].
#
# The final result then is [["Jesse", "Maybel"], ["Maggie", "Callie"]].

#
# Solution
#

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
