def scale(array, factor):

        for value in range(len(array)):
                array[value] *= factor
        
        return array


result = scale([10,20,30,2,3], 10);

print(result)