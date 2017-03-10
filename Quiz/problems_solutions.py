#
# Problem 3 - Song Playlist
#
def song_playlist(songs, max_size):
    '''
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit
    
    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat.

    return: a list of a subset of songs fitting in max_size in the order
            in which they were chosen.
    '''
    songList = []
    if songs == [] or songs[0][2] > max_size:
        return []
    else:
        songList.append(songs[0][0])
        tempSongList = songs[1:]
        orderedRemainingSongs = sorted(tempSongList, key=lambda tup: tup[2])
        currentSize = max_size - songs[0][2]
        for i in range(len(orderedRemainingSongs)):
            if currentSize - orderedRemainingSongs[i][2] < 0:
                break
            else:
                songList.append(orderedRemainingSongs[i][0])
                currentSize -= orderedRemainingSongs[i][2]
        return songList

#
# Problem 4 - Multipliers
#
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    tempMultipliers = []
    tempSum = s
    for i in range(len(L)):
        tempMultipliers.append(0)
        listInput = L[i]
        if tempSum - listInput >= 0:
            diff = tempSum - listInput
            multiplier = 1
            while diff >= 0 and diff >= listInput:
                multiplier += 1
                diff -= listInput
            tempSum = diff
            tempMultipliers[i] = multiplier
    if tempSum == 0:
        return sum(tempMultipliers)
    else:
        return 'no solution'

#
# Problem 5 - Contiguous Sum
#
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    def recur_sum(slicedL, data):
        if len(slicedL) == 1:
            data.append(slicedL[0])
            return data
        else:
            sumList = data
            count = len(slicedL)
            while count > 0:
                tempSum = sum(slicedL[0:(count)])
                sumList.append(tempSum)
                count -= 1
            return recur_sum(slicedL[1:], sumList)
    if L == []:
        return 0
    elif len(L) == 1:
        return L[0]
    else:     
        sumList = recur_sum(L, [])
        return max(sumList)    
