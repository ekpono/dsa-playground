def selection(array):
        for i in range(0, len(array) ):
                low = i
                for j in range(i, len(array)):
                        if array[low] > array[j]:
                                low = j
                
                array[i], array[low] = array[low], array[i]
        return array

array = [10,7, 2, 6, 1, 12, 9, 4, 8, 11, 5, 3]
result = selection(array)
print(result)