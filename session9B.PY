from session9A import song, playlist
def main():

    play_list = playlist()
    print("play_list is:", playlist, vars(play_list))

    song1 = song("Udd Jaa Kaale Kaava", "Udit Narayan", 4.8)
    play_list.append(song1)
    print("play_list is:", playlist, vars(play_list))

    song2 = song("Gustakhiyan", "Gurnam Bhullar", 4.5)
    play_list.append(song2)

    song3 = song("Desperado", "Raghav", 3.8)
    play_list.append(song3)

    song4 = song("Chorni", "DIVINE, Sidhu Moose Wala", 4.7)
    play_list.append(song4)

    print("Printing Playlist in Forward:")
    play_list.iterate()
    print("Printing Playlist in Backward:")
    play_list.iterate(1)

if __name__==("__main__"):
    main()