def readFile():
        result = []
        while(True):
                try:
                        value = input('Enter lines \n')
                        result.append(value)
                except EOFError:
                        result.reverse()
                        for l in result:
                                print(l)
                        break


readFile()