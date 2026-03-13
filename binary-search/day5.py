def binary(array, target):
        left = 0
        right = len(array) - 1

        while (left <= right):
                middle = (left + right) // 2

                if array[middle] == target:
                        return array[middle]
                elif array[middle] < target:
                        left = middle + 1
                else:
                        right = middle - 1
        return -1 #not found

result = binary([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
print(result)