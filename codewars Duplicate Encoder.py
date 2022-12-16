#The goal of this exercise is to convert a string to a new string where each character
# in the new string is "(" if that character appears only once in the original string,
# or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.

#Examples
#"din"      =>  "((("
#"recede"   =>  "()()()"
#"Success"  =>  ")())())"
#"(( @"     =>  "))(("


def duplicate_encode(word):
    dict_of_letters = dict()
    for letter in word:
        dict_of_letters[letter.lower()] = dict_of_letters.setdefault(letter.lower(), 0) + 1
    result=''
    for j in word:
        if dict_of_letters[j.lower()] > 1:
            result += ')'
        else:
            result += '('
    return result

#print(duplicate_encode('Success'))  ==> ")())())"
#print(duplicate_encode("recede"))  ==>  "()()()"
#print(duplicate_encode("(( @")))  ==>  "))(("
