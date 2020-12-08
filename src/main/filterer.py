# Created by Leon Hunter at 12:10 PM 12/08/2020
class Filterer(object):
    def remove_characters(self, string_to_remove_from, characters_to_remove):
        ''' TODO - Implement solution
        Given 2 arguments:
            `string_to_remove_from`, representative of the string to remove the characters from
            `characters_to_remove`, representative of the string of characters that should be removed from the `string_to_remove_from`
        return
            (case sensitive)
            a string with each character in the `characters_to_remove` removed from the string
        '''
        result = str(string_to_remove_from)
        for removeable in characters_to_remove:
            result = result.replace(removeable, '')
        return result

    def remove_vowels(self, string_to_remove_from):
        lower_case_vowels = 'aeiou'
        upper_case_vowels = lower_case_vowels.upper()
        vowels = lower_case_vowels + upper_case_vowels
        vowels_list = list(vowels)
        return self.remove_characters(string_to_remove_from, list())

    def remove_consonants(self, string_to_remove_from):
        ''' TODO - Implement solution
        Given 1 arguments:
            `string_to_remove_from`, representative of the string to remove the characters from
        return
            (case insensitive)
            a string with each character in the list `['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']` removed from the string
        '''
        return self.remove_characters(string_to_remove_from, list('bcdfghjklmnpqrstvwxyz'))

