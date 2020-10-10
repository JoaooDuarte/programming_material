#importing the regular expressions library
import re

nome = 2

regex = re.compile("%i" %(nome))

match = regex.search(input())

print(match.group())