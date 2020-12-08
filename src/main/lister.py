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
        my_list = []
        current = start
        if step == 0:
            my_list.append(start)
        else:
            while current <= stop:
                my_list.append(current)
                current = current + step
        return my_list

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
        my_list = []
        current = start
        if step == 0:
            if start % 2 == 0:
                my_list.append(start)
        else:
            while current <= stop:
                if current % 2 == 0:
                    my_list.append(current)
                current = current + step
        return my_list

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
        my_list = []
        current = start
        if step == 0:
            if start % 2 == 1:
                my_list.append(start)
        else:
            while current <= stop:
                if current % 2 == 1:
                    my_list.append(current)
                current = current + step
        return my_list
