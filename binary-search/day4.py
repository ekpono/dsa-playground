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
        return -1 # nothing was found

array = [2,4,5,6,1,6]
target = 2

result = binary(array, target)
print(result)