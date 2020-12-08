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
        result = ""
        count = 0
        while count < len(string_to_remove_from):
            if string_to_remove_from[count] in characters_to_remove:
                count = count + 1
            else:
                result = result + string_to_remove_from[count]
                count = count + 1

        return result

    def remove_vowels(self, string_to_remove_from):
        ''' TODO - Implement solution
        Given 1 arguments:
            `string_to_remove_from`, representative of the string to remove the characters from
        return
            (case insensitive)
            a string with each character in the list `['a','e',i','o','u']` removed from the string
        '''
        result = ""
        count = 0
        vowels = "aeiou"
        while count < len(string_to_remove_from):
            cond1 = string_to_remove_from[count] in vowels
            cond2 = string_to_remove_from[count] in vowels.upper()
            if cond1 or cond2:
                count = count + 1
            else:
                result = result + string_to_remove_from[count]
                count = count + 1
        return result

    def remove_consonants(self, string_to_remove_from):
        ''' TODO - Implement solution
        Given 1 arguments:
            `string_to_remove_from`, representative of the string to remove the characters from
        return
            (case insensitive)
            a string with each character in the list `['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']` removed from the string
        '''
        result = ""
        count = 0
        consonants = "bcdfghjklmnpqrstvwxyz"
        while count < len(string_to_remove_from):
            cond1 = string_to_remove_from[count] in consonants
            cond2 = string_to_remove_from[count] in consonants.upper()
            if cond1 or cond2:
                count = count + 1
            else:
                result = result + string_to_remove_from[count]
                count = count + 1
        return result
