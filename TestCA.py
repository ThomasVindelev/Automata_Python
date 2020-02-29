class ca:

    def __init__(self, startIndex, rule, generations):
        self.ca = startIndex
        self.rule = rule
        self.gen = generations
        self.dic = {0:'-', 1:'*'}
        self.ruleDic = {'111':0, '110':0, '101':0, '100':1, '011':1, '010':1, '001':1, '000':0}

    def __call__(self):
        print(''.join([self.dic[e] for e in self.ca]))

        step = 1
        while (step < self.gen):
            ca_new = []
            pattern = ''
            for i in range(len(self.ca)):

                #The entire ruleset is static, predefined and wrong
                #Needs to computate proper workings via the rule given on init
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
                ##############################
                ##############################

            print(''.join([self.dic[e] for e in ca_new]))

            self.ca = ca_new[:]

            step += 1



givenStartIndex = [
         0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0, 0,1,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,  0,0,0,0]


cc = ca(givenStartIndex, 30, 32)
cc()