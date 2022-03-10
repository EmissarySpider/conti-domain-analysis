import random

#full_sets = [bcdfghjklmnprstvwx][aeiou][bcdfghjklmnprstvwxyz][aeiou][bcdfghjklmnprstvwxyz][aeiou][bcdfghjklmnprstvwxyz]?


consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','w','x','y','z']
vowel = ['a','e','i','o','u']

"""followed by a 7th consonant:
 'pu' = always 2x"""

def createDomain():
    word = []
    #iter = 0
    for i in range(0,3):
        char1 = consonant[random.randint(0,19)]
        char2 = vowel[random.randint(0,4)]
        syllable = char1 + char2
        word.append(syllable)
    if random.randint(0,1) == 1:
        word.append(consonant[random.randint(0,19)])
        return word
    else:
        return word
    

dommy = createDomain()
print(''.join(dommy)+'.com')