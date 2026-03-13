def countingSort(array):
        max_value = max(array)
        count = [0] * (max_value + 1)

        while len(array) > 0:
                num = array.pop(0)
                count[num] += 1

        for i in range(len(count)):
                while count[i] > 0:
                        array.append(i)
                        count[i] -= 1
        
        return array
        
unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3, 100]
sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)