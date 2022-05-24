#!/usr/bin/python3

import string


def get_shift():
    _choice = input('\nDefault shift is 13, do you want to change it? [yes/no]\n\n')
    if _choice == 'yes':
        shift = input('\nHow many letters you want your text to be shifted?\n\n')
        shift = int(shift)

        if shift >= 26:
            shift = shift % 26
        
        return shift

    if _choice == 'no':
        shift = 13
        return shift

    else:
        print('\nChoice has to be "yes" or "no"')
        shift = get_shift()
        return shift


    
def decryption(shift, encrypted):

    decrypted = []
    for letter in encrypted:
        if letter in string.ascii_lowercase:

            index = string.ascii_lowercase.index(letter)
            if shift + index < 26:
                new_index = shift + index
                new_letter = string.ascii_lowercase[new_index] 
                decrypted.append(new_letter)     # has to be fixed

            if shift + index > 26:
                new_index = shift + index - 26
                new_letter = string.ascii_lowercase[new_index] 
                decrypted.append(new_letter)


        elif letter in string.ascii_uppercase:
            index = string.ascii_uppercase.index(letter)

            if shift + index < 26:
                new_index = shift + index
                new_letter = string.ascii_uppercase[new_index]
                decrypted.append(new_letter)

            if shift + index >= 26:
                new_index = shift + index - 26
                new_letter = string.ascii_uppercase[new_index]
                decrypted.append(new_letter)

        else:
            decrypted.append(letter)

    decrypted = ''.join(decrypted)

    print('\nDecrypted text:\n')
    print(decrypted)



encrypted = input('\nEnter text to be decrypted\n\n')

if __name__=='__main__':
    shift = get_shift()
    decryption(shift, encrypted)
