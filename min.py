def minValue(array):
        minVal = array[0]

        for i in range(len(array)):
                if array[i] < minVal:
                        minVal = array[i]
        
        print(minVal)


minValue([1,2,3,4,6,10,300,102,90])