def minmax(data):
        min = 0
        max = 0

        for i in range(0, len(data)):
                if data[i] < min:
                        min = data[i]
                elif data[i] > max:
                        max = data[i]
        return (min, max)

result = minmax([20,30,1,9,12, 800])

print(result)