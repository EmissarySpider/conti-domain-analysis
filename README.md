Conti Domain Parser and Pseudo-Generator

This is a WIP and I don't think they're using this exact method. DO NOT use for detection, will absolutely fire FPs.

The domains shared by CISA on 9 March 2022 look like they're kinda DGA but not totally. These scripts are sanity checking some assumptions I've made based on patterns. 

conti-domain-parser.py - reads a list of the Conti domain names (minus '.com') and checks if they match the regex. The lastCharWiggity function dumps the last characters for the 7 length strings into a text file for frequency analysis of the chars.

conti-domain-writer.py - a POC based on the regex assumptions in the domain parser script. Based on the output so far, I don't think this is exactly right, though it's possible the actors grab the most realistic words from a large dump of something like this script's outputs.

Example domain writer outputs:

mebezim.com
kosabih.com
katajog.com
keyeyel.com
cicavim.com
hodelat.com
bigusa.com
lidagub.com
homedi.com
repewiy.com
lolavu.com
bijufac.com


