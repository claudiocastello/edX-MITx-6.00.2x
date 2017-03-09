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
