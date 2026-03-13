def outOfBounce():
        indexes = [1,2,3]

        try:
                indexes[4] = 2
        except IndexError:
                print('Dont\'t try buffer overflow attacks in pythons')

outOfBounce()