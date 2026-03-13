def reversal(array):
        result = list()

        for i in range(len(array) - 1, -1, -1):
                result.append(array[i])

        return result

array = [2,3, 4, 5,2 ,3]
result = reversal(array)
print(result)

array.reverse()
print(array)