# def rangecon(start, end):
#         result = []
#         for i in range(start, end + 1, 10):
#                 result.append(i)
        
#         return result

# result = rangecon(50, 80)
# print(result)

def negativerangecon(start, end):
        return list(range(start, end - 2, -2))
        # result = []
        # for i in range(end, start + 1, -1):
        #         if i % 2 == 0:
        #                 result.append(i)
        # for i in range(start, end + 1):
        #         if i % 2 == 0:
        #                 result.append(i - ( i + i))
        
        # return result

result = negativerangecon(8, -8)
print(result)
