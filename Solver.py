class Solver:

    def demo(self, numbers):

        result = [0, 0, 0, 0]
        min=999

        split_numbers = numbers.strip().replace(" ", "").split(',')
        for x in split_numbers:
            if x.isdigit():
                if int(x)<int(min):
                    min=x
                    result[1] = int(min)
                result[0] = result[0] + 1

        return result

Solver().demo("1,2,4,6,7,8")
