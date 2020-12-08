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
        ls=[]
        for idx in range(start,stop,step):
            ls.append(idx)
        return ls

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
        int_list=self.get_integer_list(start, stop, step)
        even_list=[]
        for i in int_list:
            if i%2==0:
                even_list.append(i)
        return even_list

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
        int_list=self.get_integer_list(start, stop, step)
        odd_list=[]
        for i in int_list:
            if i%2!=0:
                odd_list.append(i)
        return odd_list