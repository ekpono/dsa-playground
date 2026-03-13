def insertion(array):
        length = len(array)

        for i in range(1, length):
                current_index = i
                current_value = array.pop(i)

                for j in range(i -1, -1, -1):
                        if array[j] > current_value:
                                current_index = j
                
                array.insert(current_index, current_value)
        return array




my_array = [64, 34, 25, 12, 22, 11, 90, 5]

inserting = insertion(my_array)
print(inserting)