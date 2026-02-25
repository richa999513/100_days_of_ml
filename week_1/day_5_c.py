#  regular expressions in python
import re

# s = 'this is my room'
# match = re.search(r'my',s)
# print(match.start())
# print(match.end())
# # here r in r'my' do not stand for regex , it stands for raw string. The raw string is slightly different from a regular string, it won’t interpret the \ character as an escape character. This is because the regular expression engine uses \ character for its own escaping purpose.

# # Function	Description
# # re.findall()	finds and returns all matching occurrences in a list
# # re.compile() 	Regular expressions are compiled into pattern objects
# # re.split() 	Split string by the occurrences of a character or a pattern.
# # re.sub()	Replaces all occurrences of a character or patter with a replacement string.
# # resubn     It's similar to re.sub() method but it returns a tuple: (new_string, number_of_substitutions)
# # re.escape()	Escapes special character
# # re.search()	Searches for first occurrence of character or pattern
# s = 'hello my kitty. this is my cat'
# print(re.findall(r'my',s))


# string = """Hello my Number is 123456789 and
#             my friend's number is 987654321"""
# regex = '\d+'
# match = re.findall(regex,string)
# print(match)

# p = re.compile('[a-e]') # Compiles a regex into a pattern object, which can be reused for matching or substitutions.
# print(p.findall("Aye, said Mr. Gibenson Stark"))

# # '\d' find all single digits
# #  '\d+' find sequence of digits
# p = re.compile('\d')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# p = re.compile('\d+')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# # \w matches a single word character.
# # \w+ matches a group of word characters.
# # \W matches non-word characters.

p = re.compile('\w')
print(p.findall("He said * in some_lang."))

p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he \
said *** in some_language."))

p = re.compile('\W')
print(p.findall("he said *** in some_language."))


# re.split() - Splits a string wherever the pattern matches. The remaining characters are returned as list elements.
# Syntax: re.split(pattern, string, maxsplit=0, flags=0)

# maxsplit (optional): Limits the number of splits. Default is 0 (no limit).
# flags (optional): Apply regex flags like re.IGNORECASE

# Consecutive Separators: If a specific separator is provided, consecutive occurrences of the separator result in empty strings in the output list in case of split function of strings
from re import split
print(split('\W+', 'Words, words , Words'))
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
print(split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))


# re.sub() - The re.sub() function replaces all occurrences of a pattern in a string with a replacement string. re.sub(pattern, repl, string, count=0, flags=0)

# count (optional): Maximum number of substitutions (default is 0, which means replace all).
# flags (optional): Regex flags like re.IGNORECASE.

# Case-sensitive replacement of all 'ub'
print(re.sub('ub', '~*', 'Subject has Uber booked already'))

# Replace only the first 'ub', case-insensitive
print(re.sub('ub', '~*', 'Subject has Uber booked already', count=1, flags=re.IGNORECASE))

# re.subn() - re.subn() function works just like re.sub(), but instead of returning only the modified string, it returns a tuple: (new_string, number_of_substitutions)
# re.subn()
# re.subn() function works just like re.sub(), but instead of returning only the modified string, it returns a tuple: (new_string, number_of_substitutions)

# Case-sensitive replacement
print(re.subn('ub', '~*', 'Subject has Uber booked already'))

# Case-insensitive replacement
t = re.subn('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE)
print(t)
print(len(t))      # tuple length
print(t[0])        # modified string

# re.escape() function adds a backslash (\) before all special characters in a string. This is useful when you want to match a string literally, including any characters that have special meaning in regex (like ., *, [, ], etc.).
# Syntax:re.escape(string)

print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))
# output - I\ Asked\ what\ is\ this\ \[a\-9\],\ he\ said\ \        \ \^WoW

# re.search() - seach for first occurence of pattern in string and return match object if found , other wise None

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24")

if match:
    print("Match at index %s, %s" % (match.start(), match.end()))
    print("Full match:", match.group(0)) # return entire mtch
    print("Month:", match.group(1)) # return match for first sub-pattern - ([a-zA-Z]+) 
    print("Day:", match.group(2)) 
else:
    print("The regex pattern does not match.")

# MAETA CHARACTERS - special characters that define search patterns.

# MetaCharacters  Description

# \   Used to drop the special meaning of character following it
# []  Represent a character class
# ^   (Caret) Matches the beginning - '^The'
# $   Matches the end - r"World!$"
# .   Matches any character except newline
# |   Means OR (Matches with any of the characters separated by it.
# ?   Matches zero or one occurrence
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate the number of occurrences of a preceding regex to match. -  a{2, 4} will be matched for the string aaab, baaaac, gaad, but will not be matched for strings like abc, bc
# ()  Enclose a group of Regex - (a|b)cd will match for strings like acd, abcd, gacd



#  [] -  [abc] will match any single a, b, or c. 
# [0, 3] is sample as [0123]
# [a-c] is same as [abc]
# [^0-3] means any character except 0, 1, 2, or 3
# [^a-c] means any character except a, b, or c




# Special Sequence        Description     Examples

# \A      Matches if the string begins with the given character       \Afor       'for geeks'

# \b      Matches if the word begins or ends with the given character. \b(string) will check for the beginning of the word and (string)\b will check for the ending of the word.      \bge        geeks

# \B      It is the opposite of the \b i.e. the string should not start or end with the given regex.      \Bge together

# \d      Matches any decimal digit, this is equivalent to the set class [0-9]        \d      123     gee1

# \D      Matches any non-digit character, this is equivalent to the set class [^0-9]     \D      geeks

# \s      Matches any whitespace character.       \s      gee ks

# \S      Matches any non-whitespace character        \S      a bd        abcd

# \w      Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_].       \w      123     geeKs4

# \W      Matches any non-alphanumeric character.     \W      >$      gee<>

# \Z      Matches if the string ends with the given regex     ab\Z        abcdab      abababab


# A Match object contains all the information about the search and the result and if there is no match found then None will be returned. Let's see some of the commonly used methods and attributes of the match object.

import re
s = "Welcome to GeeksForGeeks"
res = re.search(r"\bG", s)

print(res.re)
print(res.string)

res = re.search(r"\bGee", s)

print(res.start())
print(res.end())
print(res.span())

# start() method returns the starting index of the matched substring
# end() method returns the ending index of the matched substring
# span() method returns a tuple containing the starting and the ending index of the matched substring

# lookahead
# negative lookahead
print('negation:', re.search(r'n[^e]', 'Python'))
print('lookahead:', re.search(r'n(?!e)', 'Python')) 

# positive lookahead
import re
print('positive lookahead', re.search(r'n(?=e)', 'jasmine'))

#  Individual match as a dictionary
match = re.search(r'(?P<dd>[\d]{2})-(?P<mm>[\d]{2})-(?P<yyyy>[\d]{4})',
                  '26-08-2020')
print(match.groupdict()) # return matched result in dictionary

# Return the entire match
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020')
print(grp.group())
# Return a tuple of matched groups
print(grp.groups()) # ('26', '08', '2020') - output

# Name your groups - The re module allows you to name your groups.
match = re.search(r'(?P<dd>[\d]{2})-(?P<mm>[\d]{2})-(?P<yyyy>[\d]{4})',
                  '26-08-2020')
print(match.group('mm'))

#  Repetition ranges
print('Three Digit:', re.search(r'[\d]{3,4}', '189'))
#  open ended ranges
print(re.search(r'[\d]{1,}','5th Floor, A-118,\ Sector-136, Noida, Uttar Pradesh - 201305'))

# optional characters 
print('Color',re.search(r'colou?r', 'color')) 
print('Colour',re.search(r'colou?r', 'colour')) # u is optional

print(re.search(r'[^a-z]', 'c')) # anything except a to z at starting is exceptable
match = re.search(r'^Geek', 'Campus Geek of the month') # string starting from Geek is exceptable


