class Quicksort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self.quicksort(0, len(self.arr)-1)

    def quicksort(self, low, high):

        if low >= high:
            return

        pivot = self.partition(low, high)
        self.quicksort(low, pivot - 1)
        self.quicksort(pivot + 1, high)

    def partition(self, low, high):

        pivot = (low+high)//2

        self.arr[high], self.arr[pivot] = self.arr[pivot], self.arr[high]

        for i in range(low, high):
            if self.arr[i] < self.arr[high]:
                self.arr[i], self.arr[low] = self.arr[low], self.arr[i]
                low += 1

        self.arr[low], self.arr[high] = self.arr[high], self.arr[low]

        return low


algo = Quicksort([12, 4, -2, 1, 11, 3, 8, 5, 56, 31])
algo.sort()
print(algo.arr)
