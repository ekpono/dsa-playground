# def sumOfSquares(integerI):
#         totalSum = 0
#         for i in range(0, integerI + 1):
#                 totalSum = totalSum + (i * i)
        
#         return totalSum

# (n*(n+1)*(2*n_+1))/6

# def sumOfSquares(n):
#         return (n*(n+1)*(2*n+1))/6
                
def sumOfSquares(n):
        return sum(i**2 for i in range(1, n) if i % 2 != 0)

                



result = sumOfSquares(13)
print(result)