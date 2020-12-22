# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self, start, stop, step):
        my_list = []
        while start <= stop:
            if step == 0:
                first_list = [0]
                return first_list
            else:
                my_list.append(start)
                start += step
        return my_list


        # Given 3 integers,
        #     `start`, `stop`, and `step`
        # return a list of all integers
        #     between `start`,
        #     incrementing by `step`,
        #     up to and including `stop`
        #


    def get_even_list(self, start, stop, step):
        my_list = []
        while start <= stop:
            if step == 0:
                return my_list[0]
            elif start % 2 == 0:
                my_list.append(start)
                start += step
            else:
                start += step
        return my_list


        # Given 3 integers,
        #     `start`, `stop`, and `step`
        # return a list of all integers
        #     between `start`,
        #     incrementing by `step`,
        #     up to and including `stop`
        #     and are divisible by 2

    def get_odd_list(self, start, stop, step):
        my_list = []
        while start <= stop:
            if step == 0:
                return my_list
            elif start % 2 != 0:
                my_list.append(start)
                start += step
            else:
                start += step
        return my_list


        # Given 3 integers,
        #     `start`, `stop`, and `step`
        # return a list of all integers
        #     between `start`,
        #     incrementing by `step`,
        #     up to and including `stop`
        #     and are not divisible by 2


