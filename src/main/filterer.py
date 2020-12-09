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
        remove_char = str(string_to_remove_from)
        for remove in characters_to_remove:
            remove_char = remove_char.replace(remove, '')
        return remove_char

    def remove_vowels(self, string_to_remove_from):
        ''' TODO - Implement solution
        Given 1 arguments:
            `string_to_remove_from`, representative of the string to remove the characters from
        return
            (case insensitive)
            a string with each character in the list `['a','e',i','o','u']` removed from the string
        '''
        vowel = 'AEIOUaeiou'
        result = ''
        for char in string_to_remove_from:
          if char not in vowel:
            result = result + char
        return result


    def remove_consonants(self, string_to_remove_from):
        ''' TODO - Implement solution
        Given 1 arguments:
            `string_to_remove_from`, representative of the string to remove the characters from
        return
            (case insensitive)
            a string with each character in the list `['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']` removed from the string
        '''
        lower_conson = 'bcdfghjklmnpqrstyxvwz'
        upper_conson = lower_conson.upper()
        conson = lower_conson + upper_conson
        result = ''
        for char in string_to_remove_from:
            if char not in conson:
             result = result + char
        return result


