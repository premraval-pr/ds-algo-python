class Selection:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr)-1):
            index = i
            for j in range(i, len(self.arr)):
                if self.arr[j] < self.arr[index]:
                    index = j
            if index != i:
                self.arr[i], self.arr[index] = self.arr[index], self.arr[i]


algo = Selection([12, 4, -2, 1, 11, 3, 8, 5, 56, 31])
algo.sort()
print(algo.arr)
