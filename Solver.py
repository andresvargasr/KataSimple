class Solver:

    def demo(self, numbers):

        result = [0, 0, 0, 0]
        split_numbers = numbers.trim.replace(" ", "").split(',')
        for x in split_numbers:
            if x.isdigit():
                print(x)
                result[0] = result[0] + 1
        return result

Solver().demo("1,2,4,6,7,8")
