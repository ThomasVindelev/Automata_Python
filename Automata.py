class Automata:

    def __init__(self):
        pass

    def cellular_automation(self, string, pattern_number, generations):
        patterns = {}
        binary = [256, 128, 64, 32, 16, 8, 4, 2, 1]
        rule = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pattern_list = ["...", "..x", ".x.", ".xx", "x..", "x.x", "xx.", "xxx"]
        n = len(string)
        start =      ["..........x.........."]
        next_array = [".........xxx........."]
        next_array = ["........x...x........"]
        next_array = [".......xxx.xxx......."]
        temp = next_array

        for i in range(7, -1, -1):
            if pattern_number/(2**i) == 1:
                patterns[pattern_list[i]] = "x"
                pattern_number = pattern_number - 2**i
            else:
                patterns[pattern_list[i]] = "."

        for j in range(0, generations):
            new_string = ""
            for i in range(0, n):
                pattern = string[i-1] + string[i] + string[(i-1) % n]
                new_string = new_string + patterns[pattern]
            string = new_string
        return new_string


auto = Automata()

auto.cellular_automation("12", 30, 10)
