def insertion(array):
        n = len(array)
        for i in range(1, n):
                insert_index = i
                current_value = array.pop(i)
                for j in range(i - 1, -1, -1):
                        if array[j] > current_value:
                                insert_index = j
                array.insert(insert_index, current_value)

        return array





my_array = [64, 34, 25, 12, 22, 11, 90, 5]

inserting = insertion(my_array)
print(inserting)