def bubble(array):
        length = len(array)

        for i in range(length):
                for j in range(0, length - i - 1):
                        if array[j] > array[j + 1]:
                                array[j], array[j + 1] = array[j+1], array[j]
        
        return array


array = [3,2,1,4,6,7,5]

result = bubble(array)
print(result)