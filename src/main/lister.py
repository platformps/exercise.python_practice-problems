# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self, start, stop, step):
        number = []
        if start == stop and stop == step:
            number.append(start)
        else:
            while start <= stop:
                number.append(start)
                start += step
        return number

    def get_even_list(self, start, stop, step):
        number = []
        if start == stop and stop == step:
            number.append(start)
        else:
            while start <= stop:
                if start % 2 == 0:
                    number.append(start)
                start += step
        return number

    def get_odd_list(self, start, stop, step):
        number = []
        if start != stop and stop != step:
            while start <= stop:
                if start % 2 != 0:
                    number.append(start)
                start += step
        return number
