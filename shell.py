class Shell:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        gap = len(self.arr)//2

        while gap > 0:

            for i in range(gap, len(self.arr)):
                j = i

                while j >= gap and self.arr[j - gap] > self.arr[j]:
                    self.arr[j], self.arr[j-gap] = self.arr[j-gap], self.arr[j]
                    j -= gap

            gap = gap // 2


algo = Shell([12, 4, -2, 1, 11, 3, 8, 5, 56, 31])
algo.sort()
print(algo.arr)
