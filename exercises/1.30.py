def dividePositiveInteger():
        number = 6
        total = 0


        while number > 2:
                number /= 2
                total += 1

        return total



result = dividePositiveInteger()
print(result)