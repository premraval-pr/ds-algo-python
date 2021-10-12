class Insertion:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr)):

            j = i

            while j > 0 and self.arr[j-1] > self.arr[j]:
                self.arr[j], self.arr[j-1] = self.arr[j-1], self.arr[j]
                j -= 1


algo = Insertion([12, 4, -2, 1, 11, 3, 8, 5, 56, 31])
algo.sort()
print(algo.arr)
