import string, random

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

letter_input_1=raw_input("What letter do you want? 'v' : vowels 'c' : consonants 'l' : any letter: ")
letter_input_2=raw_input("What letter do you want? 'v' : vowels 'c' : consonants 'l' : any letter: ")
letter_input_3=raw_input("What letter do you want? 'v' : vowels 'c' : consonants 'l' : any letter: ")

def generator():
    letter1 = ""
    if (letter_input_1 == 'v'):
        letter1=random.choice(vowels)
    elif (letter_input_1 == 'c'):
        letter1=random.choice(consonants)
    elif (letter_input_1 == 'l'):
        letter1=random.choice(string.ascii_lowercase)
    else:
        letter1=letter_input_1

    letter2 = ""
    if (letter_input_2 == 'v'):
        letter2=random.choice(vowels)
    elif (letter_input_2 == 'c'):
        letter2=random.choice(consonants)
    elif (letter_input_2 == 'l'):
        letter2=random.choice(string.ascii_lowercase)
    else:
        letter2=letter_input_2

    letter3 = ""
    if (letter_input_3 == 'v'):
        letter3=random.choice(vowels)
    elif (letter_input_3 == 'c'):
        letter3=random.choice(consonants)
    elif (letter_input_3 == 'l'):
        letter3=random.choice(string.ascii_lowercase)
    else:
        letter1=letter_input_3


    # letter1=random.choice(string.ascii_lowercase)
    # letter2=random.choice(string.ascii_lowercase)
    # letter3=random.choice(string.ascii_lowercase)
    #
    # name = letter1 + letter2 + letter3

    return letter1 + letter2 + letter3

print generator()
