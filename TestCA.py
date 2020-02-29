class ca:

    def __init__(self, startIndex, rule, generations):
        self.ca = startIndex
        self.rule = rule
        self.gen = generations
        self.dic = {0:'-', 1:'*'}

    def __call__(self):
        print(''.join([self.dic[e] for e in self.ca]))

        step = 1
        while (step < self.gen):
            ca_new = []

            for i in range(len(self.ca)):

                #The entire ruleset is static, predefined and wrong
                #Needs to computate proper workings via the rule given on init
                if i > 0 and i < len(self.ca) - 1:
                    if self.ca[i - 1] == self.ca[i + 1]:
                        ca_new.append(0)
                    else:
                        ca_new.append(1)

                elif (i == 0):
                    if self.ca[1] == 1:
                        ca_new.append(1)
                    else:
                        ca_new.append(0)

                elif (i == len(self.ca)-1):
                    if self.ca[62] == 1:
                        ca_new.append(1)
                    else:
                        ca_new.append(0)
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