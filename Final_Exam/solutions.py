# Problem 3-1 / Monte Carlo Simulation

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
