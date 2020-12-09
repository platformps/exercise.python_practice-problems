# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
        '''
        if step != 0:
            result = []
            for value in range(start, stop+1, step):
                result.append(value)
            return result
        return [0]


    def get_even_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are divisible by 2
        '''
        result = []
        for value in self.get_integer_list(start, stop, step):
            is_even = value % 2 == 0
            if is_even:
                result.append(value)
        return result


    def get_odd_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are not divisible by 2
        '''
        result = []
        for value in self.get_integer_list(start, stop, step):
            is_odd = value % 2 == 1
            if is_odd:
                result.append(value)
        return result

