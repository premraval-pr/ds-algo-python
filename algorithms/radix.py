ITEMS_IN_BUCKET = 10


class Radix:
    def __init__(self, arr):
        self.arr = arr

    def get_digits(self):
        return len(str(max(self.arr)))

    def sort(self):
        for digit in range(self.get_digits()):
            self.counting_sort(digit)

    def counting_sort(self, d):
        count_arr = [[] for _ in range(ITEMS_IN_BUCKET)]

        for num in self.arr:
            index = (num // (10 ** d)) % 10
            count_arr[index].append(num)

        z = 0

        for i in range(len(count_arr)):
            while len(count_arr[i]) > 0:
                self.arr[z] = count_arr[i].pop(0)
                z += 1


algo = Radix([120, 450, 73141, 21271, 60433, 3197, 52, 5, 43589])
algo.sort()
print(algo.arr)
