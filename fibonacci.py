def fibonacci(number):
        if number == 1:
                return 1
        
        return fibonacci(number-1) + number

result = fibonacci(20)
print(result)