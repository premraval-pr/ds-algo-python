class Merge:
    @staticmethod
    def sort(arr):
        if len(arr) == 1:
            return

        # Divide
        middle_index = len(arr)//2
        left_half = arr[:middle_index]
        right_half = arr[middle_index:]

        Merge.sort(left_half)
        Merge.sort(right_half)

        # Conquer

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


list_to_sort = [12, 4, -2, 1, 11, 3, 8, 5, 56, 31]
Merge.sort(list_to_sort)
print(list_to_sort)
