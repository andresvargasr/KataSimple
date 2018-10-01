class Solver:

    def demo(self, numbers):

        result = [0, 0, 0, 0]
        min_num = 999
        max_num = 0

        split_numbers = numbers.strip().replace(" ", "").split(',')
        for x in split_numbers:
            if x.isdigit():
                if int(x) < int(min_num):
                    min_num = x
                    result[1] = int(min_num)
                if int(x) > int(max_num):
                    max_num = x
                    result[2] = int(max_num)
                result[0] = result[0] + 1

        return result

Solver().demo("1,2,4,6,7,8")
