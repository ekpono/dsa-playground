def binary_search(target, arr):
        left = 0
        right = len(arr) - 1

        while (left <= right):
                middle = (left + right) // 2

                print(middle)
                if arr[middle] == target:
                        return middle
                elif arr[middle] < target:
                        left = middle + 1
                else:
                        right = middle - 1

        return -1

# Sample sorted array and target
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = binary_search(target, arr)

print(result)