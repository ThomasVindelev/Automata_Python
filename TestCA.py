class Cellular_Automata:


    """
    Initializer for class with params giving initial state of generation
    Rule determines the binary number used to compare rows
    Generations is the number of times the algorithm will run for
    """

    def __init__(self, startIndex, rule, generations):
        self.ca = startIndex
        self.rule = rule
        self.gen = generations
        self.dic = {0:'░', 1:'█'}
        self.binary = format(rule, '08b')
        self.ruleDic = {'111':int(self.binary[0]), '110':int(self.binary[1]),
                        '101':int(self.binary[2]), '100':int(self.binary[3]),
                        '011':int(self.binary[4]), '010':int(self.binary[5]),
                        '001':int(self.binary[6]), '000':int(self.binary[7])}

    def __call__(self):

        print(''.join([self.dic[e] for e in self.ca]))

        step = 1
        while (step < self.gen):
            ca_new = []
            pattern = ''

            for i in range(len(self.ca)):

                """
                Edge case or left
                """

                if(i == 0):
                    pattern += '0'
                else:
                    pattern += str(self.ca[i-1])

                """
                Middle
                """

                pattern += str(self.ca[i])

                """
                Edge case or right
                """

                if(i == len(self.ca)-1):
                    pattern += "0"
                else:
                    pattern += str(self.ca[i+1])

                ca_new.append(self.ruleDic[pattern])
                pattern = ''

            """
            Builds string to print
            """

            print(''.join([self.dic[e] for e in ca_new]))
            self.ca = ca_new[:]

            """
            Increments generation step
            """

            step += 1

"""
Beginning sequence of numbers
This is mandatory in order for this to work
"""

givenStartIndex = [
         0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0]


cc = Cellular_Automata(givenStartIndex, 5, 23)
cc()