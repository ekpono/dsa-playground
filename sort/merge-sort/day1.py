def mergeSort(array):
        if len(array) <= 1:
            return array
        
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        sortedLeft = mergeSort(left)
        sortedRight = mergeSort(right)

        return merge(sortedLeft, sortedRight)

def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
                if left[i] < right[j]:
                       result.append(left[i])
                       i += 1
                else:
                        result.append(right[j])
                        j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result


unsortedArray = [2,1,5,9,10]

sortedArray = mergeSort(unsortedArray)

print(sortedArray)
        

                