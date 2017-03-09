# Problem 3

You are creating a song playlist for your next party. You have a collection of songs that can be represented as a list of tuples. Each tuple has the following elements:

    name: the first element, representing the song name (non-empty string)
    song_length: the second, element representing the song duration (float >= 0)
    song_size: the third, element representing the size on disk (float >= 0)

You want to try to optimize your playlist to play songs for as long as possible while making sure that the songs you pick do not take up more than a given amount of space on disk (the sizes should be less than or equal to the max_disk_size).

You decide the best way to achieve your goal is to start with the first song in the given song list. If the first song doesn't fit on disk, return an empty list. If there is enough space for this song, add it to the playlist.

For subsequent songs, you choose the next song such that its size on disk is smallest and that the song hasn't already been chosen. You do this until you cannot fit any more songs on the disk.

Write a function implementing this algorithm, that returns a list of the song names in the order in which they were chosen, with the first element in the list being the song chosen first. Assume song names are unique and all the songs have different sizes on disk and different durations.

You may not mutate any of the arguments.

For example,

    If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 12.2, the function will return ['Roar','Wannabe','Timber']
    If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 11, the function will return ['Roar','Wannabe']
    
You can start with the skeleton below.

    def song_playlist(songs, max_size):
        """
        songs: list of tuples, ('song_name', song_len, song_size)
        max_size: float, maximum size of total songs that you can fit

        Start with the song first in the 'songs' list, then pick the next 
        song to be the one with the lowest file size not already picked, repeat

        Returns: a list of a subset of songs fitting in 'max_size' in the order 
                 in which they were chosen.
        """
        
# Problem 4

You are given a list of unique positive integers L sorted in descending order and a positive integer sum s. The list has n elements. Consider writing a program that finds values for multipliers such that the following equation holds:

Assume a greedy approach to this problem. You calculate the integer multipliers m_0, m_1, ..., m_(n-1) by finding the largest multiplier possible for the largest value in the list, then for the second largest, and so on. Write a function that returns the sum of the multipliers using this greedy approach. If the greedy approach does not yield a set of multipliers such that the equation above sums to s, return the string "no solution". Write the function implementing this greedy algorithm with the specification below:

    def greedySum(L, s):
        """ input: s, positive integer, what the sum should add up to
                   L, list of unique positive integers sorted in descending order
            Use the greedy approach where you find the largest multiplier for 
            the largest value in L then for the second largest, and so on to 
            solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
            return: the sum of the multipliers or "no solution" if greedy approach does 
                    not yield a set of multipliers such that the equation sums to 's'
        """

# Problem 5

Consider a list of positive (there is at least one positive) and negative numbers. You are asked to find the maximum sum of a contiguous subsequence. For example,

    in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
    in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16

One algorithm goes through all possible subsequences and compares the sums of each contiguous subsequence with the largest sum it has seen.

Write a function that meets the specification below.

    def max_contig_sum(L):
        """ L, a list of integers, at least one positive
        Returns the maximum sum of a contiguous subsequence in L """
        #YOUR CODE HERE
    
