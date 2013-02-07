# Implementing a shuffle algorithm, then a sorting algorithm
# Fisher-Yates shuffle, quicksort
# Keith Robertson
import sys
import random
class Sort(object):  
    sorted = []
    def __init__(self, i):
        for i in range(1, i+1):
            self.sorted.append(i)
    
    def shuffle(self):
        i = len(self.sorted) - 1
        while i > 0:
            j = random.randint(0, i)
            tmp = self.sorted.pop(j)
            self.sorted.insert(j, self.sorted[i-1])
            self.sorted.pop(i)
            self.sorted.insert(i,tmp)
            i = i-1
        return self.sorted

    def sort(self):
       return self._rec_sort(self.sorted)
    
    def _rec_sort(self, L):
        if len(L) <= 1:
            return L
        pivot = L.pop(random.randint(0,len(L)-1))
        less = []
        greater = []
        for i in L:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
        return (self._rec_sort(less) + [pivot] + self._rec_sort(greater))

    def get_list(self):
        return self.sorted
    
    def set_list(self, newlist):
        if isinstance(newlist, list):
            self.sorted = newlist
        else:
            print "Bad!"

args = 100    
if len(sys.argv) > 1:
    args = int(sys.argv[1])
a = Sort(args)
print "Starting list:\n\n" + str(a.get_list()) + "\n\n"
shuffledlist = a.shuffle()
print "Shuffled list:\n\n" + str(shuffledlist) + "\n\n"
sortedlist = a.sort()
print "Sorted list:\n\n" + str(sortedlist) + "\n\n"
