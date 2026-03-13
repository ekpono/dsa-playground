def calculator():
        inputData = float(input('Enter first argument \n'))
        
        expression = input('Enter express \n')


        supportedExpression = ['*', '+', '-', '/']

        if expression not in supportedExpression:
                raise ValueError('Not the right expression')

        secondInput = float(input('Enter last argument \n'))

        if expression == '+':
                print(inputData + secondInput)
        elif expression == '*':
                print(inputData * secondInput)
        elif expression == '-':
                print(inputData - secondInput)
        elif expression == '/':
                print(inputData / secondInput)
        else:
                raise 'Something went wrong'



calculator()