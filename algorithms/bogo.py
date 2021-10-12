import random


class Bogo:

    def __init__(self, arr):
        self.arr = arr
        self.count = 0

    def is_sorted(self):
        for i in range(len(self.arr)-1):
            if self.arr[i] > self.arr[i+1]:
                return False
        return True

    def sort(self):
        while not self.is_sorted():
            self.count += 1
            print("Shuffle count: ", self.count)
            self.shuffle()

    # Fisher-Yates shuffle: we generate a new permutation in O(N)
    def shuffle(self):
        for i in range(len(self.arr)-2, -1, -1):
            j = random.randint(0, i+1)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]


algo = Bogo([1, -4, 0, 10, 12])
algo.sort()
print(algo.arr)
