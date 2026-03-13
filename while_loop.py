j = 0
hight_index = 0
data = [2,3, 200,4,5,20]

while j < len(data):
        if data[j] > data[hight_index]:
                hight_index = j
        j += 1

chr

print(data[hight_index])