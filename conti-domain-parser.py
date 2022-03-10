# Conti Domain Parser
# Reads a list of Conti domains with [.]com stripped to look for patterns
# Domain source: https://www.cisa.gov/uscert/ncas/alerts/aa21-265a
# Don't tread on my variable names

import re

def reader(domainfile: str):
    with open(domainfile, 'r') as domainsobj:
        doms = domainsobj.readlines()
        return doms


domains = reader('domainlist.txt') # I already stripped the .com because it's a distraction
counter = 0
DomList = []

def rexDomains(): #this function checks if the domain name input matches the regex and prints the sequence for each match
    
    domRex = re.compile(
        r'^[bcdfghjklmnprstvwx][aeiou][bcdfghjklmnprstvwxyz][aeiou][bcdfghjklmnprstvwxyz][aeiou][bcdfghjklmnprstvwxyz]?')
    """Char1: [bcdfghjklmnprstvwx] every consonant except q,y,z
    Char2: [aeiou] every vowel except y
    Char3: [bcdfghjklmnprstvwxyz] char1 + consonants y & z
    Char4: [aeiou]
    Chars5-6 or 5-7: more of the same, it seems. 7th char optional.
    ^[bcdfghjklmnprstvwx][aeiou][bcdfghjklmnprstvwxyz][aeiou][bcdfghjklmnprstvwxyz][aeiou][bcdfghjklmnprstvwxyz]?
    """
    
    for li in domains:
        match = domRex.match(li)
        global counter
        counter += 1
        DomList.append(match[0])
        print(counter, match[0])

rexDomains()
#print(DomList) # don't need this unless using the lastCharWiggity func

wiggity = []
def lastCharWiggity(): # wiggity whack? nah, just regular type.
    for i in DomList:
        if len(i) == 6:
            continue
        if len(i) == 7:
            lasty = i[6:]
            print(lasty)
            wiggity.append(lasty)

# Extract the last character from the 7 len strings and output to a text file to see how whack they are
"""lastCharWiggity()
wiggity.sort()
print(wiggity)
with open('out.txt', 'w') as writerObj:
    writerObj.writelines(wiggity)
    writerObj.close"""