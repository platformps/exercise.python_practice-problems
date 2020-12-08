# Created by Leon Hunter at 12:10 PM 12/08/2020
class Filterer(object):
    def remove_characters(self, string_to_remove_from, characters_to_remove):
        removed_char = ' '
        for character in string_to_remove_from:
            if character != characters_to_remove:
                removed_char += character
        return removed_char


        # Given 2 arguments:
        #     `string_to_remove_from`, representative of the string to remove the characters from
        #     `characters_to_remove`, representative of the string of characters that should be removed
        #      from the `string_to_remove_from`
        # return
        #     (case sensitive)
        #     a string with each character in the `characters_to_remove` removed from the string
        # '''


    def remove_vowels(self, string_to_remove_from):
        rem_vowel = 'AEIOUaeiou'
        result = ' '
        for char in string_to_remove_from:
            if char != rem_vowel:
                result += char
        return result

        # Given 1 arguments:
        #     `string_to_remove_from`, representative of the string to remove the characters from
        # return
        #     (case insensitive)
        #     a string with each character in the list `['a','e',i','o','u']` removed from the string
        #


    def remove_consonants(self, string_to_remove_from):
        constants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
        result = ' '
        for character in string_to_remove_from:
            if character.lower() != constants:
                result += character
        return result

        # Given 1 arguments:
        #     `string_to_remove_from`, representative of the string to remove the characters from
        # return
        #     (case insensitive)
        #     a string with each character in the list

        #     `['b', 'c', 'd', 'f',
        #       'g', 'h', 'j', 'k',
        #       'l', 'm', 'n', 'p',
        #       'q', 'r', 's', 't',
        #       'v', 'w', 'x', 'y', 'z']`

        #     removed from the string



