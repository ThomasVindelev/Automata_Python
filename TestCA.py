class ca:

    def __init__(self, startIndex, rule, generations):
        self.ca = startIndex
        self.rule = rule
        self.gen = generations
        self.dic = {0:'░', 1:'█'}
        self.binary = "{0:08b}".format(rule)
        self.ruleDic = {'111':int(self.binary[0]), '110':int(self.binary[1]), '101':int(self.binary[2]), '100':int(self.binary[3]), '011':int(self.binary[4]), '010':int(self.binary[5]), '001':int(self.binary[6]), '000':int(self.binary[7])}

    def __call__(self):
        print(''.join([self.dic[e] for e in self.ca]))

        step = 1
        while (step < self.gen):
            ca_new = []
            pattern = ''

            for i in range(len(self.ca)):

                if(i == 0):
                    pattern += '0'
                else:
                    pattern += str(self.ca[i-1])

                pattern += str(self.ca[i])

                if(i == len(self.ca)-1):
                    pattern += "0"
                else:
                    pattern += str(self.ca[i+1])

                ca_new.append(self.ruleDic[pattern])
                pattern = ''

            print(''.join([self.dic[e] for e in ca_new]))
            self.ca = ca_new[:]
            step += 1

givenStartIndex = [
         0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0, 0,1,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0]


cc = ca(givenStartIndex, 7, 21)
cc()