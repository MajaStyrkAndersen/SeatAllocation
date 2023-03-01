from itu.algs4.sorting.max_pq import MaxPQ
from itu.algs4.stdlib.stdio import readInt

class Party:
    def __init__(self, id, votes):
        self.id = id                   
        self.votes = votes                  
        self.seats = 0
        self.priority = votes // 1             
    
    def addSeats(self):
        self.seats += 1
        self.priority = self.votes // (self.seats + 1)

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return 'party'

class main():
    
    nParties = readInt()
    mSeatsAvailable = readInt()

    priorityQueue = MaxPQ(mSeatsAvailable)
    parties = []

    for i in range(nParties):
        priorityQueue.insert(Party(i, readInt())) 
        parties.append(i)

    for i in range(mSeatsAvailable):
        maxPriority = priorityQueue.del_max()
        Party.addSeats(maxPriority)
        priorityQueue.insert(maxPriority)

        mSeatsAvailable -= 1
        
    for i in parties:
        print('Number of seats: ')
        print(i)



if __name__ == "__main__":
    main()


