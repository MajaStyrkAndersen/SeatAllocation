from itu.algs4.sorting.max_pq import MaxPQ
from itu.algs4.stdlib.stdio import readInt

class Party:
    def __init__(self, id, votes):
        self.id = id                   
        self.votes = votes                  
        self.seats = 0
        self.priority = votes / 1.0             
    
    def addSeats(self):
        self.seats += 1
        self.priority = self.votes / (self.seats + 1.0)

    def __lt__(self, other):
        return self.priority < other.priority

class main():
    n_parties = readInt()
    m_seats = readInt()

    priorityQueue = MaxPQ()
    parties = []

    for i in range(n_parties):
        p = Party(i, readInt())
        priorityQueue.insert(p) 
        parties.append(p)

    for i in range(m_seats):
        maxPriority = priorityQueue.del_max()
        maxPriority.addSeats()
        #print(maxPriority.priority, maxPriority.id)
        priorityQueue.insert(maxPriority)

    for i in parties:
        print(i.seats)

if __name__ == "__main__":
    main()


