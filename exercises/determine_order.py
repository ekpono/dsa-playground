def determine_order():
        a = int(input('Enter A input \n'))
        b = int(input('Enter B input \n'))
        c = int(input('Enter C input \n'))

        if a + b == c:
                return True
        if b - c == a:
                return True
        if a * b == c:
                return True
        
        return False

istrue = determine_order()
print(istrue)