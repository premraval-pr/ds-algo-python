class Counting:
    def __init__(self, arr):
        self.arr = arr
        self.count_arr = [0 for _ in range(max(arr)-min(arr)+1)]

    def sort(self):
        for i in self.arr:
            self.count_arr[i-min(self.arr)] += 1

        z = 0

        for i in range(min(self.arr), max(self.arr)+1):
            while self.count_arr[i-min(self.arr)] > 0:
                self.arr[z] = i
                z += 1
                self.count_arr[i - min(self.arr)] -= 1


algo = Counting([12, 4, -2, 1, 11, 3, 8, 5, 56, 31])
algo.sort()
print(algo.arr)
