def bubble(array):
        total = len(array)

        for i in range(total):
                for j in range(0, total - i - 1):
                        if array[j] > array[j + 1]:
                                array[j], array[j + 1] = array[j + 1], array[j]
        return array

 
result = bubble([1,9,89,20,40,8])

print(result)