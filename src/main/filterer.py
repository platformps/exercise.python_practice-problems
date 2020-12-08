# Created by Leon Hunter at 12:10 PM 12/08/2020
class Filterer(object):
    def remove_characters(self, string_to_remove_from, characters_to_remove):
        list = ""
        for i in string_to_remove_from:
            if i not in characters_to_remove:
                list += ''.join(i)
        return list

    def remove_vowels(self, string_to_remove_from):
        list = ""
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for i in string_to_remove_from:
            if i not in vowels:
                list += ''.join(i)
        return list

    def remove_consonants(self, string_to_remove_from):
        list = ""
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U", " ", "!"]
        for i in string_to_remove_from:
            if i in vowels:
                list += ''.join(i)
        return list

