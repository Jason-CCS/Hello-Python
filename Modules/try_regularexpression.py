# ref: https://www.w3schools.com/python/python_regex.asp
import re

# Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)

if x:
    print(x)
else:
    print('no match')
