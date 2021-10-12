class Bubble():
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr)-1):
            for j in range(len(self.arr)-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]


algo = Bubble([12, 4, -2, 1, 11, 3, 8, 5, 56, 31])
algo.sort()
print(algo.arr)
