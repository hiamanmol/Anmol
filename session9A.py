class song:

    def __init__(self, track, artists, duration):
        self.track = track
        self.artists = artists
        self.duration = duration
        self.next = None
        self.previous = None

    def show(self):
        print("******************")
        print("Track name :", self.track)
        print("Artist name :", self.artists)
        print("Duration:", self.duration)
        print("Next is:", self.next, "\nPrevious is:", self.previous)
        print("******************")

class playlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, song):
        self.size += 1
        if self.head is None:
            self.head = song
            self.tail = song

        else:
            self.tail.next = song
            song.previous = self.tail
            # ANY NEWLY ADDED SONG WILL BE TAIL
            self.tail = song
            # CIRCULAR LINKED LIST
            self.head.previous = self.tail
            self.tail.next = self.head

    def iterate(self, direction=0):
        if direction == 0:
         temp = self.head
         while True:
             temp.show()
             temp = temp.next

             if temp == self.head:
                 break

        else:
            temp = self.tail
            while True:
                temp.show()
                temp = temp.previous

                if temp == self.tail:
                    break