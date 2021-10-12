print("Hello World!")

arr = [10, 3, 7, 5]

# random indexing

print("Item at index 0 = " + str(arr[0]))
print("Item at index 3 = " + str(arr[3]))
print("Item from index 0 to 2 = " + str(arr[0:2]))
print("All items without the last = " + str(arr[:-1]))

# maximum through linear search O(N) = Linear time complexity

maxi = arr[0]

for num in arr:
    if num > maxi:
        maxi = num

print("Maximum is " + str(maxi))

# print whole

print(arr)
